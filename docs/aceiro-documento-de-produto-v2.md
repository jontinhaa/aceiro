# Aceiro — Documento de produto v2
### Hackathon IAGRO 2026, Paragominas/PA

**Desafio:** "Chegada do tempo de seca: como evitar prejuízos com focos de fogo" — plataforma/app que dispare alertas geolocalizados em tempo real para vizinhos, brigadas e autoridades ao detectar um foco de incêndio.

**Tagline:** *O maior aceiro de Paragominas é a vizinhança.*

**O que mudou da v1 para a v2:** motor de alerta em níveis (relato único nunca é inválido); ligação de voz automática e árvore de escalonamento; estação de vento no kit Sentinela e arquitetura híbrida de dados meteorológicos; laudo em dois tempos (campo + órbita); posição correta frente ao Defesa Civil Alerta; arquitetura de acesso WhatsApp/painel/app; modelo financeiro com investimento por fase, unit economics e regra de caixa; mapa de incentivos; sentinelas de rota; semáforo do fundamento.

---

## 1. Resumo executivo

O Aceiro é uma plataforma de coordenação comunitária contra o fogo rural, que atua **antes, durante e depois** do foco. Ele não é um detector: é a rede que encurta o caminho entre quem vê o fogo e quem pode apagá-lo, dentro da **janela de ouro** — os primeiros 20 a 30 minutos, quando um foco ainda se apaga com abafador e enxada.

O desenho parte de uma constatação: na região, boa parte do fogo é ferramenta de trabalho (queima controlada) que escapa. Um app que "detecta e avisa autoridades" é lido como máquina de denúncia e morre por rejeição. O Aceiro inverte com a **queima declarada**: o produtor registra a queima autorizada antes; os vizinhos recebem aviso preventivo; o alerta só dispara se o fogo fugir do polígono ou horário; e o produtor ganha álibi documentado. Adoção por interesse próprio, não por civismo.

A detecção opera em **três camadas sob uma rede única**: relato humano via bot de WhatsApp (gratuito), focos públicos de satélite do INPE (gratuitos, atrasados) e o **módulo Sentinela** — câmera com visão computacional da própria equipe + estação meteorológica no mesmo mastro, vigiando o horizonte 24h a partir das sedes de quem paga (fazendas grandes, reflorestadoras). Nenhum relato é descartado: um único aviso abre investigação ativa com validação da foto por IA, ligação ao dono da área e giro de câmera — o alerta escala por score de confiança, não por contagem de testemunhas.

O produtor da base nunca paga. A receita vem de contratos B2B com interesse patrimonial direto (reflorestadora, prefeitura, seguradora/banco, projetos de carbono). A regra de caixa que governa tudo: **nenhum hardware é comprado sem contrato assinado.**

---

## 2. O problema em quatro camadas

**Física — o custo do fogo é função do tempo.** 20–30 min: abafador e enxada. 1h: pipa, trator, brigada. 3h: escolhe-se o que salvar.

**Informacional — o dado existe, mas não chega em quem age.** Satélite demora ou tem pixel grosseiro; quem vê primeiro é uma pessoa, que avisa mal (áudio sem coordenada). O gargalo é o caminho entre o olho e a enxada.

**Social — o paradoxo da confiança.** Queima controlada é prática legal. Plataforma que aciona autoridade automaticamente = dedo-duro = zero adoção. Confiança é o ativo escasso; cada decisão de desenho serve a ela.

**Econômica — o prejuízo vem depois da chama.** Cerca (gado na PA-125), curral, eucalipto, colmeia; multa, embargo, CAR travado, crédito negado; fumaça lotando UPA e fechando estrada; risco reputacional para a marca Município Verde.

*Para o pitch: focos de calor de Paragominas dos últimos dois anos no BDQueimadas/INPE — dado oficial e incontestável.*

---

## 3. A persona: Seu Raimundo

54 anos, setecentos hectares de pecuária de corte, vicinal a 35 km da sede, celular pegando só no ponto alto. Assentamento de um lado da divisa, eucalipto de reflorestadora do outro. Agosto, capim palha. Vítima potencial e causador potencial — em cima do paradoxo da confiança.

As cinco fases da dor (cada uma é uma tela do produto): **a suspeita** (cheiro de fumaça, informação zero), **a confirmação** (a coluna no horizonte — de quem é? vem para cá?), **a corrida** (peão não atende; aceiro onde? salvo o curral ou o gado do pasto 7?), **o combate às cegas** (ninguém sabe quem vem, onde tem água, onde está a frente), **o depois** (cerca, seguro sem prova, e o "foi do teu lado que veio" azedando trinta anos de vizinhança).

---

## 4. Como funciona — estados, níveis e o motor de decisão

O sistema vive em três estados. As transições têm gatilhos objetivos (score), não julgamento humano de plantão.

### Estado de Paz (nível 0 — rotina)
- Boletim diário de risco (semáforo do fogo) publicado no **Canal do WhatsApp** (transmissão gratuita) às 6h: vento, umidade, dias sem chuva, status de portaria de suspensão de queima.
- Registro de **queimas declaradas** (polígono, data, janela de horário) → aviso preventivo aos vizinhos do entorno.
- Cadastros no tempo da calma: recursos de combate (pipa, açude com status sazonal, trator, brigada, abafador), **árvore de contatos** de cada propriedade (1º dono/gerente, 2º e 3º contatos), **plano de evacuação de gado por pasto**.
- **Simulado da Seca**: um exercício anual da rede antes de agosto — alerta de treino, confirmações, teste de rota da brigada.

### Estado de Suspeita (nível 1 — investigação)
Gatilho: **um** relato humano, **uma** detecção de câmera não confirmada ou **um** foco de satélite sem queima declarada correspondente. Regra de ouro: **relato único nunca é inválido nem fica em fila de espera** — abre investigação ativa, em paralelo, em menos de 2 minutos:
1. **A foto do relato passa pelo modelo de visão computacional** (o mesmo do Sentinela): fumaça detectada na imagem soma forte no score — a IA valida relatos mesmo onde não há câmera instalada.
2. **Ligação automática ao dono/gerente da propriedade do ponto**: "recebemos indicação de fumaça no seu pasto 4 — confirma?" (confirmação eleva; negação com justificativa derruba).
3. **Giro de câmera**: qualquer Sentinela num raio de ~15 km aponta para o azimute.
4. **Contexto**: dia vermelho no índice, ausência de queima declarada, histórico do relator (reputação/Selo), proximidade de ativo (sede, reserva, rodovia).

Além disso, os 2–3 usuários mais próximos recebem aviso de verificação (círculo pequeno — falso positivo local e raro é preço aceitável; falso positivo amplo e frequente é o que mata a confiança, e o desenho impede exatamente isso).

**Score de confiança (0–100), exemplos de pesos:** fumaça na foto validada pela IA +40 · segundo relato ou confirmação de câmera +40 · confirmação do dono +40 · negação fundamentada do dono −60 · dia vermelho +15 · relator com histórico +15 · sem queima declarada +10.

**Válvula de segurança:** em dia vermelho, relato único com fumaça confirmada pela IA sobe a nível 2 por tempo (10 min sem negação), mesmo sem segunda testemunha. O custo do falso alarme local é sempre menor que o custo do fogo que cresceu esperando burocracia.

### Estado de Emergência
**Nível 2 — confirmado (score ≥ limiar):** o cone de propagação (vento + combustível + declividade) define **quem** recebe. Alerta acionável: "foco a 2,8 km NE, vento na sua direção, ~50 min até a divisa; pipa mais próximo: Fulano, a 5 km — confirmou que está indo." Canais: mensagem no WhatsApp **e ligação automática com voz sintetizada**; SMS onde só há 2G. Brigada recebe pacote padronizado: coordenada, rota, ponto de água mais próximo, contato no local. Escalonamento: sem confirmação de leitura em 5 min → liga; não atende → liga ao 2º contato da árvore.

**Nível 3 — crítico:** fogo ameaçando sede, vila, escola ou rodovia. Todos no raio recebem; a **Defesa Civil municipal é acionada com o pacote completo** — e ela, autoridade competente, pode disparar o alerta oficial no celular de todos (ver §8).

### Encerramento e pós-evento
Fogo contido → registro de quem relatou, confirmou e combateu, com horários e fotos → contorno do perímetro por GPS (bot grava a trilha de moto/a pé) → laudo (ver §6). O Selo dos participantes sobe.

---

## 5. Jornada real, minuto a minuto (cenário-referência do pitch)

Terça, agosto, dia vermelho. **14h32** motorista vê fumaça na vicinal e manda foto + localização no bot. **14h34** sem queima declarada no raio de 2 km → nível 1; IA detecta fumaça na foto (+40). **14h35** bot liga para o gerente da propriedade do ponto; câmera da reflorestadora gira para o azimute; 3 vizinhos próximos em modo verificação. **14h39** vizinho confirma com segunda foto (+40) → score estoura o limiar. **14h40** nível 2: Seu Raimundo (2,8 km, na direção do vento) recebe mensagem + ligação com voz sintetizada; abre o mapa pelo link, aciona o plano do gado (pasto 7 → pasto 2 pela porteira leste). Brigada recebe pacote: rota de 18 min, açude do Zé a 900 m. **15h05** brigada no local (~0,8 ha). **15h40** contido com trator e pipa. **Dia seguinte** perímetro contornado de moto com GPS pelo bot: 1,1 ha. **72h** laudo em PDF com linha do tempo, fotos georreferenciadas, mapa e carimbo do tempo — pronto para o seguro da cerca. Selos atualizados.

---

## 6. Funcionalidades por fase

### Antes
Queima declarada · **Ponte SEMAS** (requerimento de autorização preenchido e pronto para protocolar — v1 sem depender de API ou convênio; o bot também reflete portarias de suspensão: "queima suspensa até dd/mm") · índice de risco diário via Canal · mapa de recursos com status sazonal · plano de evacuação de gado por pasto · árvore de contatos · **Selo Aceiro** (score de prevenção da propriedade: queimas declaradas, aceiros, zero fugas → desconto em seguro e argumento de crédito; consentimento LGPD) · Simulado da Seca.

### Durante
Relato via WhatsApp (foto + GPS; conversa iniciada pelo usuário = sem custo para nós) · motor de níveis (§4) · alerta acionável com cone · **ligação de voz automática + TTS** (áudio para quem lê com dificuldade) · escalonamento pela árvore de contatos · SMS em 2G · evacuação de gado em um toque · pacote padronizado para brigada/autoridade com rota e água · detecção Sentinela 24h com humano no loop.

### Depois
**Laudo em dois tempos:** (1) **campo, 24–48h** — perímetro por GPS vira polígono com área imediata + fotos georreferenciadas + linha do tempo, com hash e **carimbo do tempo ICP-Brasil**; pronto no prazo do seguro/BO/defesa administrativa; (2) **órbita** — primeira cena limpa do Sentinel-2 (gratuita, Copernicus) roda o **dNBR** (índice de queima antes/depois, método padrão), confirmando o polígono e entregando **severidade por faixa** (a "porcentagem consumida"). A época do fogo é a época seca — chance razoável de cena limpa em dias. Radar (Sentinel-1) fica como evolução. Histórico alimenta o Selo.

---

## 7. Módulo Sentinela — câmera + estação no mesmo mastro

- **Kit por ponto:** câmera PTZ com zoom óptico varrendo 360° em ciclos + computador de borda (inferência local) + **estação meteorológica construída pela equipe** (ESP32, anemômetro, biruta, temperatura/umidade, solar) + energia solar/bateria.
- **Detecta fumaça, não chama** — a pluma é visível a quilômetros e cabe na janela de ouro.
- **Visão computacional própria:** fine-tuning de YOLO no D-Fire (dataset público brasileiro, ~21 mil imagens de fogo/fumaça). No pitch: demo com vídeo real de queimada e bounding boxes ao vivo. O mesmo modelo valida fotos de relatos humanos em toda a rede.
- **Humano no loop:** a IA propõe, uma pessoa confirma antes de alerta em massa. Posição honesta: "um olho que nunca dorme e chama gente quando desconfia" — nuvem baixa, poeira e neblina existem; o loop humano é a resposta.
- **Cobertura e dimensionamento:** a 15–20 m de altura, o horizonte geométrico é ~16 km; identificação confiável com zoom: 8–15 km. Raio de planejamento de 10 km ≈ 31 mil ha teóricos — **uma torre bem posicionada cobre uma fazenda grande**; o que quebra a conta é relevo (vale escondido), não hectare. Estudo de posicionamento com modelo de elevação gratuito (SRTM) e análise de linha de visada no QGIS — o estudo é parte do **serviço de setup cobrado**.
- **Dados de vento híbridos:** previsão gratuita de modelo global (grade) como base, **corrigida em tempo real pelos sensores locais** — resposta direta à lacuna apontada em entrevista por doutor em sensoriamento remoto (malha meteorológica insuficiente para a extensão do município). Sensor avulso (sem câmera) vira add-on barato para fazendas médias. Vento é bytes: MQTT pela internet da sede ou LoRa até ela.
- **Conectividade sem cabeamento:** Starlink/4G da sede; rádio ponto-a-ponto se o mastro ficar longe. Estruturas existentes (caixa d'água, silo, torre de internet rural) reduzem o custo do mastro a quase zero.
- **Prova de mercado:** detecção por câmera + IA já é vendida no Brasil ao setor florestal (ex.: umgrauemeio/Pantera) — valida disposição a pagar; nosso diferencial é a rede que a torre financia, com o pequeno incluído de graça.

---

## 8. Arquitetura de acesso e o problema da notificação

**Três degraus, cada um com um motivo:**
- **WhatsApp** — 90% dos usuários, 100% da emergência: relatar, receber, declarar queima, gravar perímetro. Conversa iniciada pelo usuário abre janela de serviço sem custo; alertas que iniciamos custam centavos; **boletim diário vai por Canal (gratuito)**.
- **Painel web** — "quero mais informação": mapa grande, dossiê, cadastros, gestão de brigada. Login; **não é público** (cada produtor vê a própria propriedade; brigada/prefeitura, o território — LGPD e antídoto ao dedo-duro). Link chega dentro do WhatsApp e abre no navegador.
- **App nativo (fase 2)** — existe por um único motivo decisivo: o **alarme que fura o silencioso** (critical alerts/full-screen intent) não existe via WhatsApp.

**Notificação que passa batida — resposta em camadas:** (1) disciplina de canal: rotina agrupada 1×/dia no Canal; o canal de emergência só fala quando há fogo; (2) **emergência é ligação, não mensagem** — chamada telefônica automatizada com voz sintetizada fura a pilha de grupos, funciona em 2G e custa centavos; (3) escalonamento pela árvore de contatos; (4) app fase 2 com alarme crítico.

**Defesa Civil Alerta (o alerta oficial no celular):** usa cell broadcast; no nível Extremo emite som de sirene, sobrepõe a tela e fura o silencioso; não exige app, cadastro nem internet — mas exige 4G/5G, e **só órgãos de Defesa Civil definem conteúdo e momento do disparo** (operadoras apenas transmitem). Consequência de desenho: **não prometemos integração direta** (seria promessa sem fundamento). Caminho real: **parceria institucional** — o Aceiro é a fonte qualificada da Defesa Civil municipal; em nível 3, quem aperta o botão é ela, alimentada pelo nosso dado. Ressalva a nosso favor: onde só pega 2G, nem o sistema nacional chega — quem cobre são nossa ligação de voz e SMS. Complemento de custo zero: orientar usuários a se cadastrarem nos canais oficiais (SMS com CEP para 40199, que funciona de 2G a 5G).

---

## 9. Arquitetura técnica em uma vista

```
[Pessoa em campo]──WhatsApp: foto+GPS (service, custo 0)──────┐
[Sentinelas de rota]──caminhão da madeira, ônibus escolar,────┤
                      leiteiro, mototáxi (recrutados)         │
[Satélite INPE]──focos públicos──────────────────────────────┤
[Sentinela]──câmera+YOLO na borda──confirmação humana─────────┤
[Estações de vento]──ESP32──MQTT/LoRa─────────────────────────┤
                                                              ▼
                                            [Backend Aceiro]
                            score de confiança · níveis 0–3
                            queimas declaradas (máscara) · CAR
                            cone de propagação (modelo físico
                            + vento híbrido global/local)
                                                              ▼
   ┌──────────────┬──────────────────┬─────────────────┬──────────────┐
[Vizinhos]     [Brigadas]       [Defesa Civil]      [Dossiê/Laudo]
msg + LIGAÇÃO  pacote com rota   pacote nível 3      campo 24–48h
TTS + SMS      e ponto de água   (ela aciona o        + dNBR orbital
escalonamento                    alerta oficial)      + ICP-Brasil
```

Perfis: dono e colaboradores (quem relata é o vaqueiro, sem tocar configuração).

---

## 10. Modelo de negócio e finanças

**Princípio:** usuário ≠ cliente. O produtor da base nunca paga; a receita vem de quem sangra com o fogo. **Regra de caixa: nenhum hardware sem contrato assinado** (carta de intenção/piloto pago antes da compra; o setup cobre ~metade do CAPEX do ponto).

| Plano | Para quem | Inclui | Preço (ordem de grandeza) |
|---|---|---|---|
| Rede (gratuito) | Todo produtor | Bot, alertas, queima declarada, Ponte SEMAS, mapa de recursos, INPE, Simulado, boletim via Canal | R$ 0 (custo p/ nós: < R$ 600/mês por 1.000 usuários) |
| Fazenda Pro | Fazendas grandes | Kit Sentinela em comodato (câmera + estação), evacuação de gado, laudo ICP-Brasil, Selo | Setup R$ 5–8 mil + R$ 700–1.200/mês por ponto (24–36 meses) |
| Corporativo | Reflorestadoras, carbono/REDD+, prefeitura | Multiponto com SLA, painel territorial, dados agregados | R$ 3–8 mil/mês, sob medida |
| Dados e Selo | Seguradoras e bancos | Score de prevenção (consentimento), laudo verificado, histórico | Licenciamento — receita ano 2+ |

**Por que o gratuito não pesa:** relato do usuário = janela de serviço sem custo; boletim = Canal (broadcast gratuito); pagamos só alertas que iniciamos (centavos, raros por definição). Nuvem: um servidor de R$ 100–300/mês atende milhares de usuários.

**Investimento por fase (caixa):**
- **Fase 1 — MVP software (m1–6): R$ 6–8 mil** (nuvem, API, empresa, domínio). Trabalho da equipe = sweat equity (registrar as horas: banca de negócio pergunta).
- **Fase 2 — 1º ponto Sentinela (m6–12): R$ 12–22 mil/ponto** (câmera 4–8k · edge 2–4k · mastro 3–6k ou ~0 em estrutura existente · solar 1,5–3k · instalação 1–2k) + 3 estações de vento (R$ 400–800 cada). Piloto completo: **R$ 15–25 mil — somente com contrato assinado.**

**Unit economics do ponto:** CAPEX ~R$ 18 mil − setup pago pelo cliente (R$ 6 mil) = R$ 12 mil líquidos; margem mensal ~R$ 850 (mensalidade − manutenção) → **payback 14–21 meses**, margem recorrente depois.

**Cenário base 24 meses:** âncora assina piloto pago no m7 (setup + R$ 1 mil/mês) · prefeitura m10 (R$ 3 mil/mês) · 3 fazendas Pro até m12 · expansão a 4 pontos da âncora + 10 Pro até m24 → MRR ~R$ 18 mil no m24; **equilíbrio de caixa ~m15** (sem salários de mercado no ano 1 — bootstrapping declarado). Custo acumulado m24 ~R$ 60 mil vs receita acumulada ~R$ 170 mil.

**Escalabilidade:** um município sozinho é negócio de subsistência; o retorno vem da **replicação** — custo marginal de um novo município ≈ zero na camada de software (dados públicos + WhatsApp + mesmo backend). Software escala; hardware ancora contrato e escala devagar. Rota natural: Ulianópolis, Dom Eliseu, Ipixuna, Tomé-Açu.

**Risco comercial, dito com todas as letras:** ninguém garante que o Pro vende. Por isso a sequência gasta R$ 6–8 mil para descobrir se alguém paga, antes de gastar R$ 20 mil em ferro. Se em 6 meses de MVP rodando ninguém assinar, o mercado falou — e o prejuízo coube no bolso de quem estava testando.

---

## 11. Mapa de incentivos — por que não depende de "mundo perfeito"

O modelo não pressupõe altruísmo; pressupõe interesse próprio bem alinhado:

| Ator | Motivo egoísta para participar |
|---|---|
| Reflorestadora | Ativo de 7–20 anos exposto ao fogo do vizinho; brigada já existe (custo afundado); cada fogo apagado cedo é sinistro evitado |
| Produtor médio | Alerta, álibi, requerimento SEMAS e laudo funcionam **mesmo que ele nunca ajude ninguém** — valor solo; cooperação é bônus |
| Vaqueiro | O patrão manda; o fogo ameaça o emprego |
| Vizinho que ajuda | Fogo não respeita cerca: apagar o do outro é apagar o próprio fogo futuro; reputação (Selo) e reciprocidade — instituição rural antiga (mutirão), não utopia |
| Freerider | Custa centavos; quando o fogo ameaçar **ele**, ele reporta — e o reporte serve a todos: até o egoísta é sensor |
| Prefeitura | Marca Município Verde; tempo de resposta público |
| Seguradora/banco | Menos sinistro; laudo confiável; dado de subscrição |

A cooperação nunca entra na linha de receita — lá só entram contratos B2B com interesse patrimonial mensurável.

---

## 12. Entrada no mercado e cold start

Por território, não por indivíduo: (1) **âncora** pagante (reflorestadora/fazenda grande) com interesse em que a vizinhança inteira relate cedo; (2) **distribuição** via mutirão de cadastro no sindicato/cooperativa (WhatsApp elimina a barreira de download); (3) **ativação** com o Simulado da Seca abrindo a temporada; (4) **recrutamento dos sentinelas de rota** — caminhão da madeira, ônibus escolar, leiteiro, mototáxi: quem roda a vicinal todo dia em horário fixo multiplica a cobertura das estradas sem custo de hardware.

---

## 13. Alinhamento com os critérios do edital

| Critério (peso) | Onde o Aceiro pontua |
|---|---|
| Inovação (25) | Queima declarada; motor de níveis com score (relato único nunca descartado); Ponte SEMAS; Selo; três camadas de sensor + malha de vento própria |
| Aplicabilidade (25) | WhatsApp sem download; ligação de voz que fura a pilha; evacuação de gado; SMS/2G; pacote padronizado para brigada; requerimento pronto |
| Viabilidade (20) | VC própria (YOLO + D-Fire) com demo ao vivo; comodato com payback 14–21 m; regra "sem contrato, sem ferro"; custo do gratuito < R$ 600/mês por mil usuários; comparável de mercado pagante |
| Impacto (20) | Pequeno incluído de graça; TTS para baixa alfabetização; menos área queimada e fumaça (saúde/estrada); laudo que acelera indenização; Município Verde |
| Pitch (10) | História do padrinho nas 5 fases; demo de VC ao vivo; jornada minuto a minuto; "o maior aceiro de Paragominas é a vizinhança" |

---

## 14. Roadmap com investimento por fase

- **MVP hackathon (agora):** mockup das telas casadas com as 5 fases; fluxo do bot; demo de VC em vídeo real; este plano. Caixa: ~R$ 500.
- **v1 (m1–6, R$ 6–8 mil):** bot funcional + painel + INPE + queima declarada + laudo de campo + ligação de voz. Meta: carta de intenção da âncora.
- **v2 (m6–12, R$ 15–25 mil, só com contrato):** 1º kit Sentinela instalado + 3 estações de vento + dNBR no laudo + convênio municipal.
- **v3 (ano 2):** Selo com primeira seguradora; multiponto da âncora; segundo município; app nativo com alarme crítico.
- **Visão:** sirene comunitária; sensores de estrutura (paiol/silo); parceria formal com Defesa Civil; expansão regional.

---

## 15. Semáforo do fundamento (anexo de Q&A)

| 🟢 Construímos sozinhos | 🟡 Viável, exige trabalho/dinheiro/habilidade nova | 🔴 Depende de terceiros |
|---|---|---|
| Bot (relato, alerta, queima declarada) | Sentinela em produção (vão: detecção → coordenada por azimute + relevo, ou 2ª torre) | Convênio/integração SEMAS |
| Focos INPE + mapa com CAR | dNBR / área por satélite | Disparo do Defesa Civil Alerta (só via parceria) |
| Motor de níveis + cone simples | Malha de vento além do piloto de 3–5 pontos | Seguradora aceitando laudo/Selo formalmente |
| Ligação de voz + TTS + escalonamento | App nativo com alarme crítico | Cliente carbono/REDD+ contratado |
| Requerimento SEMAS v1 | Modelo de propagação calibrado | |
| Laudo de campo + carimbo do tempo | | |
| Simulado; protótipo de estação de vento | | |

Regra do pitch: verde se demonstra; amarelo se mostra o caminho; vermelho se declara como visão com primeiro passo mapeado. Proporção atual ~60/25/15 — saudável.

---

## 16. Riscos e respostas prontas

- **"E o fogo criminoso?"** Fora do escopo prometido: resolvemos o acidental e o escapado de queima legítima (a maior parte do prejuízo do produtor); no criminoso, o alerta rápido ainda reduz dano. Escopo assumido > onipotência fingida.
- **"Relato único em área vazia não morre na burocracia?"** Não: nível 1 investiga ativamente (IA na foto, ligação ao dono, giro de câmera) e, em dia vermelho com fumaça validada, sobe por tempo. Relato nunca é descartado.
- **"E onde ninguém vê?"** Nenhum sistema detecta sem olho, câmera ou passagem de satélite — não prometemos onisciência. Mitigamos com sentinelas de rota, geoestacionário como rede de segurança tardia, e é exatamente esse vazio que vende a câmera. Prometemos que nenhum olho que viu será desperdiçado — hoje, todos são.
- **"Falso positivo não mata a confiança?"** Queima declarada mata o alarme de fogo esperado; alarme amplo só sai com score alto; falso positivo residual é local, raro e com feedback ao relator.
- **"Quem garante que o Pro vende?"** Ninguém — por isso a regra de caixa: R$ 6–8 mil para testar disposição a pagar antes de R$ 20 mil em ferro; setup do cliente financia metade do ponto.
- **"Hardware quebra no campo."** Comodato com SLA (manutenção nossa, no preço), instalação na sede (energia e internet existentes), rede funciona sem a câmera.
- **"O gratuito não vira um custo monstro?"** < R$ 600/mês por mil usuários: relato do usuário sem custo, boletim por Canal gratuito, pagamos só alertas raros que iniciamos.

---

*Equipe [nome da equipe] — Hackathon IAGRO 2026. Documento v2, aberto a correção. Números de hardware e API pedem cotação real antes do plano final.*
