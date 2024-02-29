/* Os códigos em Javascript são executados por um software chamado V8, presente em todos os navegadores. 
Além disso existe o npm, que hospeda desenvolvimento de software sob controle de versão Git. O npm gerencia pacotes para tempo de execução Javascript Node.js através do Yarn. Todas as linguagens possuem um repositório, e o npm funciona para o Javascript.

---

Muitas funções são geradas por variáveis. As variáveis em Javascript implicam em alteração de dados na memória RAM, gerando algoritmos que serão executados sempre que os valores definidos pelas variáveis forem chamados.

O Javascript costuma entregar diversas possibilidades e programas para se realizar a mesma ação; é uma característica cultural dessa linguagem.

Node.js é o verdadeiro executor do Javascript. É necessário que se instale o Node.js no PC para que se trabalhe com essa linguagem em qualquer IDE.

DICA DO PROFESSOR: Para aprender reinvente a roda, mas para trabalhar é sempre bom reutilizar a roda. Em outras palavras, use frameworks e programas já existentes para trabalhar com Javascript, nunca programando códigos do zero.

---

O código abaixo utiliza o framework "express" e a biblioteca "multer" para criar servidores online e realizar requisições web nesse servidor. 
É importante entender que as dependências do código são todas organizadas em um arquivo no formato "package.json".
Os algoritmos do código encontram o endereço IP da máquina pessoal, salvam arquivos para uma pasta selecionada (uploads/) e enviam esses arquivos para uma página estática.
Lembrando que as funções se comunicam com o documento index.html salvo neste repositório para se comunicar com o cliente.

---

Toda essa interação resume os princípios básicos da Web 2.0, a Internet convencional sem o uso do blockchain.

*/

const express = require('express');
const multer = require('multer');
const app = express();
const port = 3001;
const os = require('os');

function getLocalIpAddress() {
    const interfaces = os.networkInterfaces();
    for (const iface of Object.values(interfaces)) {
        for (const alias of iface) {
            if (alias.family === 'IPv4' && !alias.internal) {
                return alias.address;
            }
        }
    }
    return '0.0.0.0';
}

const upload = multer({ dest: 'uploads/' });


const page = express.static('public')
app.use(page);

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});


app.post('/upload', upload.single('arquivo'), (req, res) => {
    console.log(req.file);
    res.send('Arquivo recebido!');
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://${getLocalIpAddress()}:${port}`);
});
