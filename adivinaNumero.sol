pragma solidity > 0.6.1 < 0.7.0;

import "github.com/provable-things/ethereum-api/provableAPI_0.6.sol";

contract AdivinaNumero is usingProvable{
    
   address private jugador;
   uint premio;
   uint private randomnumber;
   uint private constant costoJuego = 200000000000000000; /// 0.2 ether
   address private owner;
   bool private jugando = false;
   
   /// Posteriormente, Desplegaremos un mensaje al jugador una vez que hagamos una interfaz de usuario.
   event Numeros(string, uint randomnumber, string, uint numeroAdivinado, string ,uint premio);
   
   /// Constructor
   constructor() public payable{
       owner = msg.sender;
       //// Verifica que el numero aleatorio sea seguro
       provable_setProof(proofType_Ledger);
   }
   
   function adivina() public payable {
       
       require(msg.value == 200000000000000000, "El costo del juego es de 0.2 ether." );
       require(!jugando, "Actualmente hay otro jugador, espero un momento para jugar.");
       
       /// El O corrsponde al QUERY_EXECUTION_DELAY, y siempre sera 0 pues queremos el número ASAP
       /// 1 es la cantidad de bytes que pedimos, en este caso es 1 pues solo queremos un número
       /// 200000 el Gas necesario para ejecutar la función callback
       provable_newRandomDSQuery(0, 1, 200000); 
  
   }
    
    //Sobreescritura del callback para la API de Provable.
    function __callback(bytes32 _queryId, string memory _result, bytes memory _proof) public override {
        require(msg.sender == provable_cbAddress());
        require(provable_randomDS_proofVerify__returnCode(_queryId, _result, _proof) == 0, "Uno de los números aleatorios generados no es confiable.");
        /// Generamos el número aleatorio
        randomnumber = ((uint256(keccak256(abi.encodePacked(_result))) % 10) + 1);
    }
    
    /// Tenemos esta otra función que guarda la lógica del juego pues el número aleatorio se genera de manera asíncrona.
   function jugar( uint numeroAdivinado) public payable {
       
       /// Gas para generar los números aleatorios
       require((msg.value == 200000), "Para jugar envíe 200000 wei." );
       
       if(numeroAdivinado == randomnumber){
            jugador = msg.sender;
            premio = 1000000000000000000;
        }
        else{
            premio = 0;
        }
        /// Desplegamos el mensaje
        emit Numeros("El numero generado fue:",randomnumber,"Tu escogiste:",numeroAdivinado,"Ganaste:", premio);
   }
}
