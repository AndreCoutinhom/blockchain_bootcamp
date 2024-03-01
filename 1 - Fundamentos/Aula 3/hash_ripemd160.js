/* Funções hash podem ser encontradas em grande número na biblioteca "crypto". 
Elas se diferem na evolução da tecnologia de criptografia que pode ser mais fácil ou mais difícil de invadir, facilidade de uso, etc.

---

Neste código, a função hash é selecionada e dados são inseridos e "hasheados" de forma que sejam criptografados com saída de tamanho fixo.

*/

const crypto = require('crypto');

function hashRIPEMD160(inputString) {
  return crypto.createHash('ripemd160').update(inputString).digest('hex');
}

const inputString = 'Hello, world!';
console.log('RIPEMD-160:', hashRIPEMD160(inputString));
