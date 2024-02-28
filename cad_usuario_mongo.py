import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QVBoxLayout, QPushButton
from pymongo import MongoClient

client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")

# selecionando o banco de dados loja_db
db = client.loja_db


class CadUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Cadastro de usuarios")

        labelUsuario = QLabel("Nome Usuário:")
        self.editUsuario = QLineEdit()

        labelSenha = QLabel("Senha:")
        self.editSenha = QLineEdit()

        labelNivel = QLabel("Nível:")
        self.editNivel = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")

        self.labelMsg = QLabel("|")

        layout = QVBoxLayout()
        layout.addWidget(labelUsuario)
        layout.addWidget(self.editUsuario)

        layout.addWidget(labelSenha)
        layout.addWidget(self.editSenha)

        layout.addWidget(labelNivel)
        layout.addWidget(self.editNivel)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.cadUs)

        layout.addWidget(self.labelMsg)

        self.setLayout(layout)

    def cadUs(self):
        usuario_id = db["usuario"].insert_one({"nomeusuario":self.editUsuario.text(),"senha":self.editSenha.text(),"nivel":self.editNivel.text()}).inserted_id
        self.labelMsg.setText("Usuário Cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadUsuario()
    tela.show()
    sys.exit(app.exec_())        