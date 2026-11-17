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
