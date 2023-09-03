import numpy as np
from PIL import Image

def png_to_stl(png_file, stl_file):
    # PNG dosyasını yükle
    image = Image.open(png_file)
    # PNG görüntüsünü siyah beyaz formata dönüştür
    image = image.convert('L')
    # Görüntüyü Numpy dizisine dönüştür
    data = np.array(image)
    height, width = data.shape

    # STL dosyasını oluştur
    with open(stl_file, 'w') as f:
        f.write('solid STL_model\n')

        # Her piksel için STL üçgenlerini oluştur
        for i in range(height - 1):
            for j in range(width - 1):
                # Dört köşe noktasını al
                p1 = [j, i, data[i, j]]
                p2 = [j + 1, i, data[i, j + 1]]
                p3 = [j + 1, i + 1, data[i + 1, j + 1]]
                p4 = [j, i + 1, data[i + 1, j]]

                # STL üçgenlerini oluştur
                f.write('facet normal 0 0 0\n')
                f.write(f'    outer loop\n')
                f.write(f'        vertex {p1[0]} {p1[1]} {p1[2]}\n')
                f.write(f'        vertex {p2[0]} {p2[1]} {p2[2]}\n')
                f.write(f'        vertex {p3[0]} {p3[1]} {p3[2]}\n')
                f.write(f'    endloop\n')
                f.write(f'endfacet\n')

                f.write('facet normal 0 0 0\n')
                f.write(f'    outer loop\n')
                f.write(f'        vertex {p3[0]} {p3[1]} {p3[2]}\n')
                f.write(f'        vertex {p4[0]} {p4[1]} {p4[2]}\n')
                f.write(f'        vertex {p1[0]} {p1[1]} {p1[2]}\n')
                f.write(f'    endloop\n')
                f.write(f'endfacet\n')

        f.write('endsolid STL_model\n')

    print(f'{png_file} STL formatına dönüştürüldü: {stl_file}')

# Örnek kullanım
png_to_stl('rose.png', 'cikis.stl')