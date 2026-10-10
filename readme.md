on_delete deve ser cascade, pois ao autor parar o relacionamento com o sistema o sistema perde também os direitos autorais deste autor.

1. Que dados se perdem quando a migração é revertida? Por quê?
é perdido os autores, pois eles estão em outra tabela, a não ser que crie uma logica de reversão a tabela autores sera Null

2. Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?
tem algumas formas, a primeira é implementação manual do CASCADE, buscando os livros que tem apenas ele como autor e exlcuindo junto ou bloqueando a exclusão desse autor até a exclusão ou edição de todos livros que ele participe, assim como no metodo save ter uma checagem de pelo menos um autor setado
