/* Funções hash podem ser encontradas em grande número na biblioteca "crypto". 
Elas se diferem na evolução da tecnologia de criptografia que pode ser mais fácil ou mais difícil de invadir, facilidade de uso, etc.

---

Neste código, a função hash é selecionada e dados são inseridos (no caso aqui está sendo a string "Hello World") e "hasheados" de forma que sejam criptografados com saída de tamanho fixo.

*/

const crypto = require('crypto');

function hashBLAKE2b(inputString) {
  return crypto.createHash('blake2b512').update(inputString).digest('hex');
}

const inputString = 'Hello, world!';
console.log('BLAKE2b:', hashBLAKE2b(inputString));
