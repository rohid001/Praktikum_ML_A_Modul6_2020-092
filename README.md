# ⚡️ Klasifikasi dan Preediksi Rock-Paper-Scissors ⚡️

## Overview Arsitektur Model
Aktivitas dalam project ini adalah melakukan klasifikasi rock, paper, dan scissors

***Link Dataset yang digunakan :*** [Rock-Paper-Scissors data set](https://drive.google.com/file/d/1IVejv65VlMB8lV5iCmhkEw6A4rKV03Lh/view?usp=drive_link)
Preprocessing yang digunakan: Augmentasi, Resizing, Rotation, dan Horizontal Flip

Model yang digunakan: Convolutional Neural Network 2D dengan 15 layer seperti pada gambar dibawah ini:
![model_CNN h5](https://github.com/rohid001/Praktikum_ML_A_Modul6_2020-092/assets/98394099/007febca-1ad3-4106-90cf-9d09faa47951)

## Overview Dataset
***Link Dataset yang digunakan :*** [Rock-Paper-Scissors data set](https://drive.google.com/file/d/1IVejv65VlMB8lV5iCmhkEw6A4rKV03Lh/view?usp=drive_link)
Gambar yang digunakan adalah representasi rock, paper, dan scissors dalam bentuk tangan dengan total gambar 2520 gambar. Terdiri dari 840 gambar Paper, 840 Rock, dan 840 Scissor

Splitting Dataset : Training = 70%, Validation = 25%, dan Testing = 5%

## Preprocessing dan Modelling
- **Preprocessing Model : rescale = 1./255, validation split = 0.5, shear range = 0.2, zoom range = 0.2, rotation range = 20, horizontal flip = True
- Modelling Model:

  Summary model:

  ![Screenshot 2023-12-12 045948](https://github.com/rohid001/Praktikum_ML_A_Modul6_2020-092/assets/98394099/245f7d6f-796a-49c7-bd22-64df3e817517)

  Graph Loss dan Accuracy Model
  
  ![loss dan accuracy](https://github.com/rohid001/Praktikum_ML_A_Modul6_2020-092/assets/98394099/1bbf3552-4979-4430-81d7-c09c25fa3ffd)

