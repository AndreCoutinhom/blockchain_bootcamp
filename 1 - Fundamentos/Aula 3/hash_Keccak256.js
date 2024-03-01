/* Funções hash podem ser encontradas em grande número na biblioteca "crypto". 
Elas se diferem na evolução da tecnologia de criptografia que pode ser mais fácil ou mais difícil de invadir, facilidade de uso, etc.

---

Neste código, a função hash é selecionada e dados são inseridos e "hasheados" de forma que sejam criptografados com saída de tamanho fixo.

*/

const crypto = require('crypto');

function hashKeccak256(inputString) {
  return crypto.createHash('sha3-256').update(inputString).digest('hex');
}

const inputString = 'Hello, world!';
console.log('Keccak265:', hashKeccak265(inputString));
