import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QStyle, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

class GuiDuasColunas(QWidget):

    def __init__(self):
        super().__init__()

        self.total = 0.0
        self.linha = 0

        self.setGeometry(5,25,1600,840)
        self.setWindowTitle("Caixa da Padaria")

        layoutVerEs = QVBoxLayout()
        layoutVerDi = QVBoxLayout()
        layoutHor = QHBoxLayout()

        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#c5873e;}")
        labelColEsq.setFixedWidth(800)

        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#efab53;}")
        labelColEsq.setFixedWidth(800)

        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("Padaria.jpg"))
        labelLogo.setScaledContents(True)

        labelCodigo = QLabel("Código do Produto:")
        labelCodigo.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.codigoEdit = QLineEdit()
        self.codigoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelNomeProduto = QLabel("Nome do Produto:")
        labelNomeProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.nomeProdutoEdit = QLineEdit()
        self.nomeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelDescricao = QLabel("Descrição do Produto:")
        labelDescricao.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.DescricaoProdutoEdit = QLineEdit()
        self.DescricaoProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelQuantidade = QLabel("Quantidade do Produto:")
        labelQuantidade.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.QuantidadeProdutoEdit = QLineEdit()
        self.QuantidadeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelPrecoProduto = QLabel("Preço Unitário do Produto:")
        labelPrecoProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.PrecoProdutoEdit = QLineEdit()
        self.PrecoProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelSubTotalProduto = QLabel("Sub Total:")
        labelSubTotalProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.SubTotalProdutoEdit = QLineEdit("Aperte F3 para calcular o subtotal")
        # Desabilitar a caixa do subtotal
        self.SubTotalProdutoEdit.setEnabled(False)
        self.SubTotalProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")


        layoutVerEs.addWidget(labelLogo)
        layoutVerEs.addWidget(labelCodigo)
        layoutVerEs.addWidget(self.codigoEdit)
        
        layoutVerEs.addWidget(labelNomeProduto)
        layoutVerEs.addWidget(self.nomeProdutoEdit)

        layoutVerEs.addWidget(labelDescricao)
        layoutVerEs.addWidget(self.DescricaoProdutoEdit)

        layoutVerEs.addWidget(labelQuantidade)
        layoutVerEs.addWidget(self.QuantidadeProdutoEdit)

        layoutVerEs.addWidget(labelPrecoProduto)
        layoutVerEs.addWidget(self.PrecoProdutoEdit)
        
        layoutVerEs.addWidget(labelSubTotalProduto)
        layoutVerEs.addWidget(self.SubTotalProdutoEdit)

        labelColEsq.setLayout(layoutVerEs)

        # Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(10)

        # Criando o cabecalho para a tabela resumo
        titulos = ["Código","Nome Produto","Quantidade","Preço Unitário","Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)

        labelTotalPagar = QLabel("Total a Pagar:")
        labelTotalPagar.setStyleSheet("QLabel{color:black;font-size:25pt}")
        self.totalPagarEdit = QLineEdit("0,00")
        self.totalPagarEdit.setEnabled(False)
        self.totalPagarEdit.setStyleSheet("QLineEdit{padding:10px;font-size:50pt}")

        layoutVerDi.addWidget(self.tbResumo)
        layoutVerDi.addWidget(labelTotalPagar)
        layoutVerDi.addWidget(self.totalPagarEdit)

        layoutVerDi.addWidget(self.tbResumo)
        labelColDir.setLayout(layoutVerDi)


        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)

        self.setLayout(layoutHor)

        # Capturando a tecla que o usuario esrá digitando e chamando a funçao(keyPressEvent)
        # para executar um comando quando esta tecla for acionada.
        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):

        
        
        if(e.key() == Qt.Key_F2):
            print(' Você teclou F2')
            self.tbResumo.setItem(self.linha,0,QTableWidgetItem(str(self.codigoEdit.text())))
            self.tbResumo.setItem(self.linha,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,2,QTableWidgetItem(str(self.QuantidadeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,3,QTableWidgetItem(str(self.PrecoProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,4,QTableWidgetItem(str(self.SubTotalProdutoEdit.text())))
            self.linha+=1
            self.total+=float(self.SubTotalProdutoEdit.text())
            self.totalPagarEdit.setText(str(self.total))

            # Limpar os LineEdit
            self.codigoEdit.setText("")
            self.nomeProdutoEdit.setText("")
            self.DescricaoProdutoEdit.setText("")
            self.QuantidadeProdutoEdit.setText("")
            self.PrecoProdutoEdit.setText("")
            self.SubTotalProdutoEdit.setText("Aperte F3 para calcular o subtotal")
        elif(e.key() == Qt.Key_F3):
            qtd = self.QuantidadeProdutoEdit.text()
            prc = self.PrecoProdutoEdit.text()
            res = float(qtd) * float(prc)
            self.SubTotalProdutoEdit.setText(str(res))    
app = QApplication(sys.argv)
janela = GuiDuasColunas()
janela.show()
app.exec_()