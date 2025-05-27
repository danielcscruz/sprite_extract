from PIL import Image
import os
import zipfile

# Configurações
sprite_size = 24
input_path = "slime_green.png"
output_dir = "sprites_24x24"
zip_name = "sprites_24x24.zip"

# Criar pasta de saída
os.makedirs(output_dir, exist_ok=True)

# Abrir imagem com canal alpha
image = Image.open(input_path).convert("RGBA")
width, height = image.size

rows = height // sprite_size
cols = width // sprite_size

for row in range(rows):
    for col in range(cols):
        box = (col * sprite_size, row * sprite_size, (col + 1) * sprite_size, (row + 1) * sprite_size)
        sprite = image.crop(box)
        sprite.save(f"{output_dir}/sprite_{row}_{col}.png")

# Criar arquivo .zip
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for filename in os.listdir(output_dir):
        zipf.write(os.path.join(output_dir, filename), arcname=filename)
