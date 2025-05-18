![Ilustração de uma mulher concentrada no laptop, simbolizando foco, produtividade e trabalho com inteligência artificial.](https://github.com/user-attachments/assets/574b6d0b-435a-42ba-b9cb-89039076a1c7)
# 📚 Agentes de IA para Otimização de Estudos: Uma Jornada com Alura e Google Gemini 🚀
## ✨ Motivação: Otimizar meus estudos utilizando IA
Durante a Imersão IA da Alura, em parceria com o Google Gemini, recebemos o desafio de desenvolver um projeto que mostrasse como os Agentes de Inteligência Artificial podem ser aplicados para resolver problemas do dia a dia. Pensando na minha própria rotina de estudos, percebi o quanto seria útil ter um assistente que me ajudasse a encontrar conteúdos relevantes e a organizar meu tempo de forma mais eficiente. Foi daí que nasceu a ideia deste projeto: criar um assistente inteligente que torne o aprendizado mais prático, focado e produtivo.

## 💡 A Solução Proposta: Uma Arquitetura de Agentes Colaborativos
Este projeto representa uma exploração prática na construção de sistemas multi-agentes utilizando o Google Agent Developer Kit (ADK) e a Google Gemini API. A solução consiste em dois agentes de IA interconectados, cada um com uma responsabilidade específica, colaborando para gerar um guia de estudo personalizado:

1. Primeiro Agente: Agente Curador de Recursos 🕵️‍♀️

   * Propósito: Este agente atua como um especialista em pesquisa de conteúdo. Sua função é receber um tópico de estudo e, utilizando a Google Search Tool, identificar e selecionar os recursos online mais confiáveis e de alta qualidade.
   * Critérios de Curadoria: A inteligência do agente foi instruída a priorizar fontes com alta autoridade, como artigos acadêmicos, sites de instituições de ensino, publicações científicas e canais educativos renomados, filtrando conteúdos menos confiáveis como blogs pessoais não referenciados ou fóruns genéricos.
   * Saída: Uma lista concisa de 3 a 5 links relevantes (artigos, vídeos, tutoriais), cada um com uma breve descrição do seu conteúdo.

2. Segundo Agente: Agente Planejador de Foco 🧠

   * Propósito: Uma vez que os recursos são selecionados pelo Agente Curador, este agente assume a tarefa de criar um plano de estudo estruturado. Ele recebe a lista de recursos e o tempo total que o usuário tem disponível para estudar.
   * Metodologia Pomodoro Integrada: O planejador é instruído a dividir o tempo total em "sprints" focadas (inspiradas na técnica Pomodoro, com 25 minutos de estudo intenso seguidos por 5 minutos de pausa).
   * Alocação Inteligente de Recursos: Ele distribui os recursos entre as sprints de forma lógica, considerando a duração estimada de cada um (especialmente para vídeos) e sugere objetivos claros para cada período de foco.
   * Engajamento: Para tornar o estudo mais leve, o plano é enriquecido com mensagens motivacionais e um "desafio bônus".
  
## 🧗‍♀️ Desafios e Aprendizados
Criar esse projeto foi uma experiência de aprendizado intensa e cheia de desafios e descobertas. Como ainda estou construindo minha base em programação e em arquitetura de agentes, precisei pesquisar bastante para entender como estruturar agentes que realmente colaborassem entre si de forma funcional.

Um dos maiores desafios foi definir uma lógica clara de cooperação entre os agentes e ajustar suas instruções para que o resultado final fizesse sentido. Foi preciso muito teste, tentativa e erro para que cada agente entendesse seu papel e entregasse algo que realmente contribuísse para a proposta final do projeto.

Por outro lado, consegui entender na prática como agentes especializados podem se complementar para alcançar um objetivo comum. Aprendi que instruções bem definidas são capazes de realizar coisas incríveis através de um prompt bem elaborado, bem como a importância de realizar vários testes antes de chegar em um resultado desejado. 

Essa jornada me tirou da zona de conforto, mas também me mostrou o quanto a inteligência artificial pode ser uma forte aliada no meu processo de aprendizado.

## 💻 Como Executar o Projeto
Você pode experimentar os agentes de IA no seu próprio ambiente. Siga os passos abaixo para baixar e executá-los:

1. Pré-requisitos:
   * Uma conta Google.
   * Uma [API Key](https://aistudio.google.com/app/apikey?utm_source=website&utm_medium=referral&utm_campaign=Alura-may-25) do Google Gemini.
   * Recomenda-se o uso do [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb) para uma experiência mais fluida.

2. Download do Projeto:
   * Baixe o arquivo do projeto [clicando aqui](https://github.com/nagelamartins/projeto-agente-IA/blob/main/Projeto_Agente_de_IA_Alura_e_Gemini.ipynb)
  
3. Configuração da API Key:
   * Faça upload do arquivo `.ipynb` para o seu Google Colab.
   * Adicione sua `GOOGLE_API_KEY` nas "Secrets" do Colab (ícone de chave na barra lateral), nomeando-a `GOOGLE_API_KEY`.
  
4. Execução:
   * Com o arquivo aberto no Google Colab:
     - Execute todas as células do notebook sequencialmente (Ctrl+Enter ou Shift+Enter).
     - O notebook irá guiá-lo, solicitando o tópico de estudo e o tempo disponível.
     - Observe os agentes trabalhando para gerar os recursos e o plano de estudo!

## 🚀 Próximos Passos
Minhas ideias para melhorias futuras incluem:

- [ ] Integração com Calendário: Enviar o plano de estudo diretamente para agendas digitais.
- [ ] Interface Web: Criar uma interface mais amigável para o uso desses agentes.
- [ ] Integração com Google Drive: Permitir criar arquivos de resumos do que foi estudado e enviá-los para o Google Drive.

## 🤝 Contribuições
Sinta-se à vontade para sugerir melhorias ou reportar issues. Este é um projeto de aprendizado e toda contribuição é bem-vinda!

## 📧 Contato
  * Nagela Martins Souza
  * [LinkedIn](https://www.linkedin.com/in/nagela-martins-7a8576337/)
  * [GitHub](https://github.com/nagelamartins)


 


  
   
