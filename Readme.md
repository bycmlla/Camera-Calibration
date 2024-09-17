## CALIBRAÇÃO DA CÂMERA IMX219-83 

<img align="center" alt="IMX219 Camera" width="400px" src="https://www.waveshare.com/img/devkit/accBoard/IMX219-83-Stereo-Camera/IMX219-83-Stereo-Camera-details-size.jpg"/>

**O que é a calibração de câmera estéreo?**

A calibração de câmera estéreo é um processo fundamental para sistemas de visão por computador que utilizam duas ou mais câmeras para captar imagens de um mesmo ambiente. O objetivo é determinar a relação entre as câmeras e o ambiente para que as imagens capturadas possam ser combinadas para criar um modelo tridimensional preciso.

**Como é feita?**

A calibração de câmeras estéreo envolve a determinação dos parâmetros intrínsecos e extrínsecos de duas câmeras dispostas em uma configuração estéreo. Os parâmetros intrínsecos descrevem as propriedades ópticas de cada câmera individual, enquanto os parâmetros extrínsecos descrevem a posição e a orientação relativas entre as câmeras.

Para realizar a calibração intrínseca, foram capturadas algumas imagens de um tabuleiro de xadrez (8x6) em várias posições e orientações com a câmera 0. Também é possível utilizar o mesmo código para calibração com imagens da câmera 1.

<img align="center" alt="stereo setup" width="400px" src="https://souri.sh/assets/images/blog/stereo_calibration/1.png"/>

Code using the Python programming language together with the OpenCV library.

The images in the repository are copyrighted images.
