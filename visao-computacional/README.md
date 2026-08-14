# Visão computacional

Detecção de **fumaça** (não de chama — a pluma é visível a quilômetros e cabe na janela de ouro dos primeiros minutos).

- Arquitetura: YOLO com fine-tuning
- Dataset: D-Fire (público, brasileiro, ~21 mil imagens anotadas de fogo e fumaça)
- Execução: inferência na borda, junto à câmera
- **Humano no loop:** a IA propõe, uma pessoa confirma antes de qualquer alerta em massa

O mesmo modelo valida as fotos enviadas por relato humano no WhatsApp, o que estende a verificação automática para toda a rede — inclusive onde não há câmera instalada.

# O que fazer para usar:

- Caso queira uma demonstração rápida, escola o "aceiro_treinado". Ele já está funcional pronto para identificar a fumaça.
- O outro arquivo "aceiro_metodo" é todo o projeot de treinamento alpha. Demorará ~2 horas para o treinamento.

- Video está com o nome "demo", se atente para o nome do vídeo que está nos códigos.

_O best.pt será essencial para rodar no uso do "aceiro_treinado"._

_Qualquer dúvida, entrar em contato com :(91) 98534-7535 ou jhonatanmatos070@gmail.com // jhonatanalmeida4306@gmail.com_
