# Visão computacional

Detecção de **fumaça** (não de chama — a pluma é visível a quilômetros e cabe na janela de ouro dos primeiros minutos).

- Arquitetura: YOLO com fine-tuning
- Dataset: D-Fire (público, brasileiro, ~21 mil imagens anotadas de fogo e fumaça)
- Execução: inferência na borda, junto à câmera
- **Humano no loop:** a IA propõe, uma pessoa confirma antes de qualquer alerta em massa

O mesmo modelo valida as fotos enviadas por relato humano no WhatsApp, o que estende a verificação automática para toda a rede — inclusive onde não há câmera instalada.

## Arquivos

_(notebook de treino e vídeos de demonstração entram aqui)_
