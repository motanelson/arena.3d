from PIL import Image

def main():
    # Perguntar o nome do ficheiro
    input_filename = input("Digite o nome do ficheiro (com extensão .bmp, .png ou .jpg): ").strip()
    
    try:
        # Abrir a imagem
        img = Image.open(input_filename).convert("RGBA")
        print(f"Imagem carregada: {input_filename} ({img.size[0]}x{img.size[1]})")
    except FileNotFoundError:
        print("Ficheiro não encontrado. Verifique o nome e tente novamente.")
        return
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return

    # Criar nova imagem com transparência baseada na condição
    new_img = Image.new("RGBA", img.size)
    
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b, a = img.getpixel((x, y))
            if r > 221 and g < 48 and b < 48:
                new_img.putpixel((x, y), (r, g, b, 0))  # Totalmente transparente
            else:
                new_img.putpixel((x, y), (r, g, b, a))

    # Criar o novo nome do ficheiro
    output_filename = "new_" + input_filename

    # Salvar a nova imagem
    try:
        new_img.save(output_filename)
        print(f"Nova imagem salva como: {output_filename}")
    except Exception as e:
        print(f"Erro ao salvar a nova imagem: {e}")

if __name__ == "__main__":
    main()

