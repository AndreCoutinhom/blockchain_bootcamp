/* Curvas elípticas em criptografia são o processo principal para criação de chaves.
O que acontece é uma refatoração de resultados por modelos complexos de matemática, para que a leitura dos dados retorne em uma saída exclusiva.

---

O código abaixo serve como roteiro para criação de chaves e necessita da instalação da biblioteca "elliptic". 
Use o comando: npm install elliptic
*/

const elliptic = require('elliptic');

const ec = new elliptic.ec(secp256k1);

const keyPair = ec.genKeyPair();

const privateKey = keyPair.getPrivate('hex');

const publicKey = keyPair.getPublic('hex');

console.log('Chave privada:', privateKey);
console.log('Chave pública:', publicKey);

const message = 'Mensagem para assinar';
const signature = keyPair.sign(message);

consol.log('Assinatura válida?', keyPair.verify(message, signature));
