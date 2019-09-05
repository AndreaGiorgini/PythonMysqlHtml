from flask_table import Table, Col, LinkCol
 
class Results(Table):
    tarefa_id = Col('Id', show=False)
    tarefa_titulo = Col('Titulo')
    tarefa_descricao = Col('Descricao')
    tarefa_status = Col('Status')
    edit = LinkCol('Editar', 'edit_view', url_kwargs=dict(id='tarefa_id'))
    delete = LinkCol('Apagar', 'delete_tarefa', url_kwargs=dict(id='tarefa_id'))

# para criar o a tabela no banco de dados
# CREATE TABLE `tbl_tarefa` (
#   `tarefa_id` bigint(20) NOT NULL AUTO_INCREMENT,
#   `tarefa_titulo` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
#   `tarefa_descricao` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
#   `tarefa_status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A', -- A(aberta), C(cancelada), D(desenvolvendo), F (finalizada)
#   PRIMARY KEY (`tarefa_id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
