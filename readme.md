on_delete deve ser cascade, pois ao autor parar o relacionamento com o sistema o sistema perde também os direitos autorais deste autor.

1. Que dados se perdem quando a migração é revertida? Por quê?
é perdido os autores, pois eles estão em outra tabela, a não ser que crie uma logica de reversão a tabela autores sera Null

2. Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?
tem algumas formas, a primeira é implementação manual do CASCADE, buscando os livros que tem apenas ele como autor e exlcuindo junto ou bloqueando a exclusão desse autor até a exclusão ou edição de todos livros que ele participe, assim como no metodo save ter uma checagem de pelo menos um autor setado


o django avisa que não tem a proteção e por isso ele não terminara a requisição sendo barrado nos middlewares, o from obrigatoriamente no django necessita do csfr junto para validar a requisição




1.2. Perguntas
a) O LivroModelForm mudou? Por que as regras do Model funcionam nele e no Admin sem nenhuma alteração?
não pois os validadores estam no model, ja que é um modelform a checagem deve estar no model, e por isso os validadores são checados tanto no livromodelform quanto no form do admin
b) Qual é a diferença entre um validator e o método clean_<campo>()? Dê um exemplo de regra que só pode ser feita com clean_<campo>().
 validator checa uma condição sem mudar o valor, o clean pode tratar um campo (como por exemplo um .strip())
c) Para cada regra, diga qual estratégia usar: argumento do campo, validators=[...], clean_<campo>() ou clean(). Justifique.
O título não pode ser igual ao nome do autor.
validator pois é uma checagem
O título deve ser salvo sem espaços no início e no fim.
clean, ele altera o campo para atender os requisitos
O número de páginas deve ser no máximo 5000.
validator pois ele é uma checagem que barra caso nn satisfeito
Um livro "indisponível" precisa ter o ISBN preenchido.
validator


2.2. Perguntas
a) O que acontece se esquecermos request.FILES na view? E se esquecermos o enctype no template? Reproduza os dois erros e descreva o que viram (o formulário dá algum aviso?).
a imagem não é salva, e não tem avisos dependendo da modelagem do banco, se a imagem for um campo obrigatorio avisara que não foi preenchido pelo usuario, mas caso seja opconal então o formulario vai fazer apenas as outras validações
b) Qual é a diferença entre STATICFILES_DIRS / {% static %} e MEDIA_ROOT / .url? Quando usar cada um na Mini biblioteca?
static são do sistema, algo interno feito ja pelo desenvolvendor, o media é dados dinamicos enviados pelos usuarios
c) Ao excluir um livro (ou trocar a capa), o arquivo antigo continua em media/capas/. Por que isso acontece e que problema pode causar a longo prazo?
pois não tem uma rotina de remoção automatica executada no update, ou delete de uma capa, isso pode virar um problema pois pode inflar rapidamente o espaço do banco de dados
d). Por que a extensão do arquivo não basta como proteção? Que outros cuidados o servidor deve ter com uploads?
a extensão do arquivo é algo mais visual, o que realmente é validavel é o header que mostra para o computador como ele deve interpretar os bytes, seja por cor (imagens) ou instruções (executaveis)

3.1. Perguntas

a) Na CreateView, quem faz o if request.method == "POST" que escrevíamos à mão? O que acontece quando o formulário é inválido?
o metodo post da classe, quando é invalido ele é tratado pelo form_isclean()

b) Por que o upload da capa continuou funcionando na CreateView sem passarmos request.FILESmanualmente?
pois o metodo post ja envia tanto o request.FILE quanto o request.POST
c) Por que o DeleteView mostra uma página de confirmação e só exclui no POST? Que problema aconteceria se a exclusão ocorresse em um GET?
se fosse no get um redirecionamento errado ou alguem enviando alguma forma de GET ou ate mesmo cliques errados poderiam gerar a exclusão
d) Cite uma vantagem e uma desvantagem das CBVs em relação às FBVs. Em que situação você ainda escolheria uma função?
a vantagem é ter varias coisas ja prontas, e que voce so vai mudar aquilo que precisa mudar, mas em situações como precisar somente renderizar uma view ou uma logica de negocio muito especifica que não seria tão verbosa eu ainda iria preferir as FBV


SQLite vs. PostgreSQL: SQLite é embutido em arquivo local (sem servidor, baixa concorrência, ideal para testes/MVPs simples); PostgreSQL é servidor cliente-servidor robusto (alta concorrência, ACID, tipos avançados, ideal para produção/multi-usuário).

Driver e instalação: Django usa psycopg (v3) ou psycopg2-binary; instale com pip install psycopg[binary] ou pip install psycopg2-binary.

Chaves do DATABASES: ENGINE define o backend (django.db.backends.postgresql), NAME é o nome do banco, USER é o usuário, PASSWORD é a senha, HOST é o endereço/serviço e PORT é a porta (padrão 5432).

Banco e usuário próprio: No psql como superusuário, rode CREATE USER app_user WITH PASSWORD 'senha'; e CREATE DATABASE app_db OWNER app_user;.

Variáveis de ambiente: Valores injetados no ambiente do SO/container fora do código-fonte para não vazar segredos no Git, facilitar deploy e variar config por ambiente.

Ler .env no settings.py: Chame load_dotenv() (com python-dotenv) ou config() (com python-decouple) no topo do settings.py e leia via os.environ["CHAVE"] / config("CHAVE").

.gitignore e .env.example: .gitignore impede o commit de .env (segredos) e db.sqlite3; .env.example versiona as chaves esperadas com valores fictícios para orientar outros devs.

Outras configs sensíveis/ambientais no settings.py: SECRET_KEY, DEBUG (False em prod), ALLOWED_HOSTS, credenciais de e-mail/cache/APIs externas e URLs de banco/storage.