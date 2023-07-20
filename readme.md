## Preprocessing Images for Retinal Photography

python version : 3.9.7
requirements : opencv-python

```bash
pip install opencv-python
```

## Usage

```bash
python preprocess_image.py <image_path>
# example) python preprocess_image.py sample_image.png
```

## Results - preview step by step
### Input Image
<img src='sample_image.png' width=300px>

### Step1 : Conver image into grey scale
<img src='step1.png' width=300px>

### Step2 : Remove black area from the image
<img src='step2.png' width=300px>

### Step3 : Apply contrast enhancement
<img src='step3.png' width=300px>

### Step4 : Make image square 
<img src='step4.png' width=300px>

### Step5 : Crop circle to remove outliers from image
<img src='step5.png' width=300px>

### Step6 : Crop top and bottom to make images equal
<img src='step6.png' width=300px>

