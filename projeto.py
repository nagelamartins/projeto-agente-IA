# Importando bibliotecas
!pip -q install google-genai

# Configurando a API Key do Google Gemini
import os
from google.colab import userdata
os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

# Configurando o cliente da SDK do Gemini
from google import genai
client = genai.Client()
MODEL_ID = "gemini-2.0-flash"

# Instalando o Framework de agentes do Google
!pip install -q google-adk

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings
warnings.filterwarnings("ignore")

# ----- FUNÇÕES AUXILIARES -----
# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
    # Cria um serviço de sessão em memória
    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Cria um Runner para o agente
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria o conteúdo da mensagem de entrada
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response

# Função auxiliar para exibir texto formatado em Markdown no Colab
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

##########################################
# --- Agente 1: Curador de recursos --- #
##########################################

def agente_curador_recursos(topico):
    agente_curador = Agent(
        name="agente_curador",
        model= MODEL_ID,
        instruction="""
        Você é um especialista em encontrar os melhores e mais confiáveis recursos online para estudo.
        Sua tarefa é receber um tópico de estudo do usuário e, usando a ferramenta de busca do Google (Google_search),
        encontrar e listar 3 a 5 links relevantes para artigos, vídeos, tutoriais ou explicações
        que ajudem o usuário a aprender sobre o tópico.

        **Priorize fontes de alta qualidade e autoridade no assunto.
        ** Procure por:
        * Artigos acadêmicos ou de pesquisa: De universidades, institutos de pesquisa ou periódicos científicos.
        * Sites de instituições de ensino: Universidades, escolas, plataformas educacionais renomadas.
        * Livros didáticos ou e-books reconhecidos: Se puder encontrar links para acesso ou informações sobre eles.
        * Canais educativos renomados no YouTube ou outras plataformas: Canais de professores, universidades, ou portais de ciência/educação.
        * **Evite:** Blogs pessoais sem referência, fóruns de discussão (a menos que sejam de especialistas), sites de notícias generalistas (a menos que citem fontes primárias).

        Formate sua resposta como uma lista numerada de links, cada um com uma breve descrição do que o recurso oferece.
        Exemplo:
        1. [Título do Artigo] - Breve descrição do conteúdo (URL do Artigo)
        2. [Título do Vídeo] - Explica sobre X assunto (URL do Vídeo)
        """,
        description="Agente que encontra e lista recursos online (artigos, vídeos, tutoriais) sobre um tópico de estudo, priorizando fontes confiáveis.",
        tools=[google_search]
    )
    entrada_agente_curador = f"Tópico que quero estudar: {topico}"
    recursos_encontrados_string = call_agent(agente_curador, entrada_agente_curador)
    return recursos_encontrados_string 

######################################
# --- Agente 2: Planejador de foco --- #
######################################

def agente_planejador_foco(tempo_total, recursos_encontrados_string):
    agente_planejador = Agent(
        name="agente_planejador_foco",
        model= MODEL_ID,
        instruction="""
        Você é um mestre da produtividade e um planejador de sessões de estudo.
        Sua tarefa é receber uma lista de recursos de estudo (links e descrições)
        e o tempo total disponível do usuário para estudar (ex: "2 horas", "45 minutos").

        Com base nesses dados, crie um plano de estudo detalhado, dividindo o tempo em "sprints" focadas
        (sugestão: 25 minutos de estudo intenso + 5 minutos de pausa, estilo Pomodoro),
        alocando os recursos para cada sprint. Tente distribuir os recursos de forma lógica e
        sugira o que o usuário deve fazer em cada sprint (ex: "Sprint 1: Ler o Artigo X").

         **Ao planejar, considere a duração estimada dos recursos, como vídeos, e aloque tempo suficiente para eles nas sprints.
         **Se um vídeo tem 15 minutos, por exemplo, ele deve ocupar uma parte proporcional da sprint.

        Formate o plano de forma clara, usando cabeçalhos para cada sprint e bullet points.
        Adicione um toque motivacional ou um pequeno "desafio" no final do plano para encorajar o usuário.

        Exemplo de formato:
        --- Plano de Estudo Focado ---
        Tempo Total Disponível: [Tempo do Usuário]

        Sprint 1 (25 min de estudo + 5 min de pausa):
        * Objetivo: Ler o Artigo sobre [Assunto] (link: https://pt.wikipedia.org/wiki/Artigo_%28gram%C3%A1tica%29)
        * Foco: Compreender os conceitos básicos de...

        Sprint 2 (25 min de estudo + 5 min de pausa):
        * Objetivo: Assistir o vídeo sobre [Assunto] (link: https://www.youtube.com/letsdovideo)
        * Foco: Anotar pontos chave e exemplos.

        [... outras sprints ...]


        Acrescente um Desafio Bônus ao final e uma frase encorajadora. 
        Por exemplo:
        Desafio Bônus: Ao final, tente explicar o conceito principal para si mesmo em voz alta!
        Não desanime! É aos poucos que o conhecimento é construído! 💪
        """,
        description="Agente que cria planos de estudo focados em 'sprints' com base em recursos e tempo disponível.",
        tools=[]
        )
     
    entrada_agente_planejador = f""" Recursos de estudo: {recursos_encontrados_string}
    Tempo total disponível: {tempo_total}
    """
    sprints = call_agent(agente_planejador, entrada_agente_planejador)
    return sprints

# ---- LÓGICA DO SISTEMA DE AGENTES ----

print("Olá! Vamos criar seu Guia de Estudo Focado. 🎯📚")

topico = input("Qual tópico você gostaria de estudar hoje? (ex: 'Python para iniciantes'): ")
tempo_total = input("Quanto tempo você tem para estudar hoje? (ex: '2 horas', '1 hora e 45 minutos'): ")


if not topico:
    print("Você esqueceu de digitar o tópico! Por favor, tente novamente.")
elif not tempo_total:
    print("Você esqueceu de digitar o tempo de estudo! Por favor, tente novamente.")
else:
    print(f"\nÓtimo! Vamos buscar recursos online sobre '{topico}' e criar um plano de {tempo_total} para te auxiliar nos estudos!")

    try:
        recursos_encontrados_string = agente_curador_recursos(topico)

        print("\n--- 📚 Aqui estão os recursos que encontrei para você: ---\n")
        display(to_markdown(recursos_encontrados_string))
        print("--------------------------------------------------------------")

        # Pequena validação: Se não houver recursos, não faz sentido gerar o plano
        if not recursos_encontrados_string or len(recursos_encontrados_string.strip()) < 20: 
            print("\n⚠️ Não foi possível encontrar recursos suficientes. O plano de estudo não será gerado.")
            print("Tente um tópico de estudo diferente ou verifique sua API Key/conexão.")
        else:
            print(f"\nGerando seu plano de estudo focado para {tempo_total}...")

            # Chamando o Agente Planejador de Foco
            plano_final_string = agente_planejador_foco(tempo_total, recursos_encontrados_string)

            print("\n--- Seu Plano de Estudo Focado ---")
            display(to_markdown(plano_final_string))
            print("--------------------------------------------------------------")

        print("\n--- Processo Concluído! Bons estudos! ✨ ---")

    except Exception as e:
        print(f"\n⛔ Ocorreu um erro inesperado: {e}")
        print("Isso pode ser um problema com a API, sua conexão ou nas instruções dos agentes. Tente novamente.")
