#include <Wire.h>			// libreria para bus I2C
#include <Adafruit_GFX.h>		// libreria para pantallas graficas
#include <Adafruit_SSD1306.h>		// libreria para controlador SSD1306
 
#define ANCHO 128			// reemplaza ocurrencia de ANCHO por 128
#define ALTO 64				// reemplaza ocurrencia de ALTO por 64

#define OLED_RESET 4			// necesario por la libreria pero no usado
Adafruit_SSD1306 oled(ANCHO, ALTO, &Wire, OLED_RESET);	// crea objeto

//Configuracion de Pines Sensor de color
// 5   ---> VCC
//GND  ---> OE
//GND  ---> GND
//12   ---> S2
//11   ---> S3
//10   ---> OUT
// 9   ---> S1
// 8   ---> S0

//Pines de Pantalla OLED
//GND ---> GND
//VCC ---> 5V
//SDA ---> A4
#define S0 8
#define S1 9
#define S2 12
#define S3 11
#define salidaSensor 10
int Lectura[3];
int R,G,B,F;
//pesos obtenidos para perceptron 1 y 2
float p1p1 = 42.80000000000001;
float p1p2 = 4.600000000000016;
float p1p3 = -28.899999999999984;

float p2p1 = -225.6000000000002;
float p2p2 = 123.80000000000007;
float p2p3 = -1.6999999999999886;

int P1,P2;//Si los perceptrones se activan o no



void setup() {
  //Salidas
  pinMode(S0,OUTPUT);
  pinMode(S1,OUTPUT);
  pinMode(S2,OUTPUT);
  pinMode(S3,OUTPUT);

  //Entrada
  pinMode(salidaSensor,INPUT);

  //escala de la Frecuencia a 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);

  //comunicacion en serie
  Serial.begin(9600);
  Wire.begin();					// inicializa bus I2C
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3C);	// inicializa pantalla con direccion 0x3C

}

void Dibujar(int R, int G, int B, int F){// funcion que actualiza la pantalla
  String red = String(R);//recibe los colores
  String green = String(G);
  String blue = String(B);
  oled.clearDisplay();//limpia lo que haya en la pantalla
  oled.setTextColor(WHITE);
  oled.setCursor(0, 0);
  oled.setTextSize(1);
  Fruit(F);
  //u8g2.drawFrame(1, 5, 36, 13);
  oled.drawRect(1, 5, 36, 13, WHITE);
  oled.drawRect(1, 21, 36, 13, WHITE);
  oled.drawRect(1, 37, 36, 13, WHITE);
  oled.setCursor(6, 14-7);
  oled.print("Rojo");
  oled.setCursor(4, 32-8);
  oled.print("Verde");
  oled.setCursor(6, 48-8);
  oled.print("Azul");
  //imprime los valores leidos por el sensor
  oled.setCursor(42, 14-7);
  oled.print(red);
  oled.setCursor(42, 32-8);
  oled.print(green);
  oled.setCursor(42, 48-8);
  oled.print(blue);

  
  
  oled.display();//genera el fotograma
}

void Fruit(int F){//funcion que escribe en la pantalla dependiendo de los datos del sensor
  oled.drawRect(64, 11, 60, 37, WHITE);

  if(F == 0){
      oled.setCursor(68, 33-8);
      oled.print("Mandarina");
  }
  if(F == 1){
      oled.setCursor(79, 33-8);
      oled.print("Limon");
  }
  if(F == 2){
      oled.setCursor(74, 33-8);
      oled.print("Manzana");
  }

  if(F == 3){
      oled.setCursor(79, 33-8);
      oled.print("Error");
  }

}

int LeerColor(int tiempo_de_espera){//funcion que obtiene los colores con el sensor
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  //leer la frecuencia de salida del sensor
  Lectura[0]=pulseIn(salidaSensor,LOW);
  delay(tiempo_de_espera);

  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  //leer la frecuencia de salida del sensor
  Lectura[1]=pulseIn(salidaSensor,LOW);
  delay(tiempo_de_espera);

  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  //leer la frecuencia de salida del sensor
  Lectura[2]=pulseIn(salidaSensor,LOW);
  delay(tiempo_de_espera);

  return Lectura;//regresa un arreglo
}

int Perceptron1(int R, int G, int B ){//funcion para evaluar si el perceptron 1 se activa o no
  float n = 0.4 + R*p1p1 + G*p1p2 + B*p1p3;
  if (n>=0){
    return 1;
  }else{
    return 0;
  }
}

int Perceptron2(int R, int G, int B ){//funcion para evaluar si el perceptron 2 se activa o no
  float n = 0.4 + R*p2p1 + G*p2p2 + B*p2p3;
  if (n>=0){
    return 1;
  }else{
    return 0;
  }
}

//Para clasificar se considera lo siguiente: Objeto (perceptron 1,perceptron 2)
// Manzana (0,0)
// Limon (1,0)
// Mandarina (0,1)
int Clasificar(int R, int G, int B){//funcion que clasifica que fruta es y regresa un valor dependiendo de la fruta
  P1 = Perceptron1(R,G,B);
  P2 = Perceptron2(R,G,B);

  if(P1 == 1){
    if(P2 == 1){
      Serial.println("Fuera de Rango");// Nada (1,1)
      return 3;
    }
    if(P2 == 0){
      Serial.println("Es una limon!!");// Limon (1,0)
      return 1;
    }
  }

  if(P1 == 0){
    if(P2 == 1){
      Serial.println("Es un mandarina!!");// Mandarina (0,1)
      return 0;
    }
    if(P2 == 0){
      Serial.println("Es una manzana");//Manzana (0,0)
      return 2;
    }
  }

}

void loop() {
  int* lectura;//se declara el arreglo para  la lectura
  lectura = LeerColor(200);//se obtienen los valores del sensor
  //se imprimen por consola los valores obtenidos
  Serial.print(lectura[0]);
  Serial.print(" ");
  Serial.print(lectura[1]);
  Serial.print(" ");
  Serial.println(lectura[2]);
  //se clasifica que fruta es con los valores del sensor
  F = Clasificar(lectura[0],lectura[1],lectura[2]);
  Dibujar(Lectura[0],Lectura[1],Lectura[2],F);//se muestra en el display los valores obtenidos y la fruta obtenida
  delay(1000);
}
