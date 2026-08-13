# Aceiro — prévia técnica do projeto

**Contexto:** conceito desenvolvido para o Hackathon IAGRO 2026 (Paragominas/PA), no desafio "Chegada do tempo de seca: como evitar prejuízos com focos de fogo".

**Objetivo deste documento:** apresentar de forma resumida como o sistema funcionaria e expor as premissas e lacunas técnicas em aberto, para crítica e orientação.

---

## 1. Em uma frase

O Aceiro é uma plataforma de coordenação comunitária contra o fogo rural: ele encurta o caminho entre **quem detecta o foco** e **quem pode apagá-lo**, dentro da janela em que o combate ainda é barato — os primeiros 20 a 30 minutos.

A premissa de partida é que o gargalo não está na detecção em si, mas na chegada da informação a quem pode agir. Os dados de focos existem e são públicos, mas terminam em painéis que ninguém no campo consulta, enquanto o vizinho a 500 metros — a única pessoa capaz de agir na janela útil — descobre pela fumaça.

---

## 2. O ponto sensível do desenho: fogo é ferramenta de trabalho

Boa parte do fogo na região não é acidente: é queima de limpeza ou renovação de pasto, muitas vezes com autorização ambiental. Isso significa que uma plataforma que apenas detecta e notifica autoridades tende a ser lida pelo produtor como mecanismo de denúncia — e não é adotada.

A resposta de desenho é a **queima declarada**: o produtor registra previamente a queima autorizada (polígono, data, janela de horário). Com isso, o sistema (a) não dispara alarme para fogo esperado dentro do polígono e do horário, (b) avisa preventivamente os vizinhos e (c) fornece ao produtor um registro documentado caso o fogo escape. O alerta só é gerado quando o foco está fora do que foi declarado.

Essa decisão tem consequência direta para o tratamento de dado: o polígono declarado funciona como máscara de supressão de alarme, e o cruzamento entre foco detectado e declaração vigente é o filtro principal contra falso positivo operacional.

---

## 3. Arquitetura de detecção — três camadas

O sistema não depende de uma única fonte. São três camadas com custo, latência e cobertura diferentes, integradas em uma base geográfica comum.

**Camada 1 — Relato humano (via bot de WhatsApp).**
Quem detecta primeiro, na prática, é uma pessoa em campo. O relato entra por WhatsApp (sem necessidade de instalar aplicativo) com foto e localização, gerando um ponto com coordenada, horário e evidência visual. Latência: imediata. Cobertura: onde há gente. Custo: zero para o usuário.

**Camada 2 — Focos de calor de satélite (dados públicos do INPE / Programa Queimadas).**
Consumo dos focos já processados (coordenada, satélite de origem, horário, confiança), plotados no mesmo mapa. Serve como cobertura de fundo, contexto regional e histórico. Latência: de dezenas de minutos a horas, conforme o sensor. Custo: zero.

**Camada 3 — Módulo "Sentinela" (câmera fixa com visão computacional).**
Câmera PTZ em mastro no ponto alto da sede, varrendo o horizonte em ciclos, com processamento na borda. O modelo é treinado para detectar **pluma de fumaça**, não chama — a fumaça é o que se enxerga a quilômetros e o que cabe na janela útil. Pretendemos treinar o modelo por conta própria (fine-tuning de uma rede de detecção sobre o dataset público brasileiro D-Fire). A detecção passa por **confirmação humana** antes de gerar alerta em massa. Latência: contínua, inclusive de madrugada — que é o vão que as outras duas camadas não cobrem. Custo: instalação e assinatura, viável apenas para propriedades maiores.

A lógica das três camadas é de complementaridade: a camada gratuita atende todos os produtores, inclusive os pequenos; a câmera cobre o período noturno onde há investimento que a justifique.

---

## 4. O que o sistema faz com o dado

**Antes do fogo.** Registro de queimas declaradas; índice diário de risco a partir de variáveis meteorológicas (vento, umidade, dias sem precipitação); cadastro georreferenciado de recursos de combate da vizinhança (caminhão-pipa, açudes, tratores, brigadas); rotas de evacuação de rebanho pré-configuradas por pasto.

**Durante o evento.** O alerta não informa apenas a existência do foco, mas a sua relação com quem recebe: distância, direção, estimativa de tempo até a divisa. A estimativa de propagação seria feita por um modelo físico simplificado, com vento, condição do combustível e declividade — sem pretensão de sofisticação, apenas de utilidade e defensabilidade. O alerta é distribuído por notificação, SMS (onde só há 2G) e áudio sintetizado, e aciona brigadas com coordenada, rota de acesso e ponto de água mais próximo.

**Depois do evento.** Consolidação de um dossiê georreferenciado — pontos de detecção, fotos com coordenada e horário, linha do tempo, declaração de queima vigente, estimativa de área atingida — destinado a uso em seguro rural, boletim de ocorrência e defesa administrativa.

---

## 5. Premissas que assumimos (e que gostaríamos de ver testadas)

Listamos abertamente o que estamos assumindo sem validação técnica formal. São exatamente os pontos em que uma correção seria mais valiosa para nós.

1. **Latência e resolução do satélite.** Assumimos que os produtos de foco de calor disponíveis não chegam a tempo, nem com precisão suficiente, para orientar ação no nível de talhão — e que por isso a camada humana e a câmera são necessárias. Não sabemos quantificar isso com rigor.

2. **Omissão de focos pequenos.** Assumimos que fogo rasteiro e queima de pequena extensão frequentemente não são detectados por satélite. Se isso se confirmar, é o principal argumento técnico a favor do nosso desenho.

3. **Geolocalização a partir da câmera.** Este é o nosso maior vão. A câmera detecta a pluma; não sabemos qual é o método adequado e a margem de erro realista para converter essa detecção em coordenada — se é possível com uma torre única (azimute combinado com modelo digital de elevação) ou se seria necessária triangulação com duas ou mais.

4. **Modelo de propagação.** Assumimos que um modelo físico simples é preferível, num protótipo, a um modelo estatístico treinado — já que não dispomos de histórico local rotulado. Não sabemos quais variáveis são realmente indispensáveis nem em que resolução os dados de entrada estão disponíveis para a região.

5. **Estimativa de área queimada.** Assumimos que é possível estimar a área atingida por imagem orbital após o evento, mas suspeitamos que a cobertura de nuvens da região possa inviabilizar o prazo necessário para uso em laudo. Precisamos entender o método padrão e o tempo realista.

6. **Atribuição de foco a propriedade.** Pretendemos cruzar focos com geometrias do CAR. Não sabemos a magnitude do erro de atribuição — e este é um risco social sério: apontar a propriedade errada pode gerar conflito real entre vizinhos.

7. **Validação da detecção.** Não temos definido qual métrica de acerto e de falso alarme seria exigível para considerar a detecção confiável.

---

## 6. O que consideramos o diferencial

Não é a detecção — detecção de fogo por câmera e por satélite já existe e já é comercializada. O que estamos propondo é a camada de coordenação: transformar dados dispersos em ação combinada de vizinhança, com um mecanismo (a queima declarada) que evita que a ferramenta seja rejeitada socialmente, e com uma camada de acesso gratuito que inclui o pequeno produtor, que hoje está fora de qualquer sistema de monitoramento.

---

*Equipe [nome da equipe] — Hackathon IAGRO 2026. Documento preliminar, aberto a correção.*
