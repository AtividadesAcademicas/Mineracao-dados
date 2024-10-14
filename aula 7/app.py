import os  
from openai import AzureOpenAI  

endpoint = os.getenv("ENDPOINT_URL", "URL")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4-32k")
subscription_key = os.getenv("CHAVE", "CHAVE")

pergunta = input("Digite sua pergunta: ")

'''Pergunta realizada: 'Quais os produtos do Microsoft Office?'

   Resposta retornada: '1. Microsoft Word - Um processador de texto com várias funcionalidades, como edição de texto, gráficos, imagens, etc.\n\n2. Microsoft Excel - Uma poderosa ferramenta de planilha para análise de dados, cálculos, gráficos e muito mais.\n\n3. Microsoft PowerPoint - Software para criação de apresentações de slides com suporte para multimídia, animações e várias outras funcionalidades.\n\n4. Microsoft Outlook - Cliente de e-mail que também inclui um calendário, gerenciador de tarefas, gerenciador de contatos e notas.\n\n5. Microsoft Access - Sistema de gerenciamento de banco de dados que permite criar e gerenciar bancos de dados para várias finalidades.\n\n6. Microsoft Publisher - Um programa de publicação de desktop que ajuda a criar materiais de marketing de qualidade profissional.\n\n7. Microsoft OneNote - Um aplicativo de anotações digitais que permite capturar e organizar notas.\n\n8. Microsoft Teams - Plataforma de comunicação que combina bate-papo persistente, videoconferências, armazenamento de arquivos e integração de aplicativos.\n\n9. Microsoft SharePoint - Plataforma de colaboração que permite compartilhar e gerenciar conteúdo, conhecimento e aplicativos para promover o trabalho em equipe.\n\n10. Microsoft Visio - Uma ferramenta de diagramação e gráficos vetoriais.\n\n11. Microsoft Project - Software de gerenciamento de projetos para planejar, gerenciar e entregar projetos.\n\n12. Microsoft OneDrive - Serviço de armazenamento em nuvem que permite aos usuários armazenar arquivos e dados pessoais.\n\nTodos esses produtos podem ser adquiridos individualmente ou como parte do pacote Microsoft 365.'
'''

client = AzureOpenAI(
    azure_endpoint = endpoint,
    api_key = subscription_key,
    api_version = "2024-05-01-preview",
)

completion = client.chat.completions.create(
    model=deployment,
    messages= [{"role": "user", "content": pergunta}],
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())