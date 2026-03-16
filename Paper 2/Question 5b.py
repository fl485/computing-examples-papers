import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

file_name = 'Paper 2\southwing.jpg'
image = img.imread(file_name)
if image.ndim == 3:
    image = np.mean(image, axis=2)

image_height, image_width = image.shape

kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
kernel_dim = len(kernel)

output_h = image_height - kernel_dim + 1
output_w = image_width - kernel_dim + 1
convoluted_image = np.zeros((output_h, output_w))

for i in range(output_h):
    for j in range(output_w):
        region = image[i:i+kernel_dim, j:j+kernel_dim]
        convoluted_image[i][j] = np.sum(kernel * region)

convoluted_image = np.clip(convoluted_image, 0, 255)



fig, axes = plt.subplots(1, 2)

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(convoluted_image, cmap='gray')
axes[1].set_title('Edge Detection')
axes[1].axis('off')

plt.show()
fig.savefig('convolved.jpg')
