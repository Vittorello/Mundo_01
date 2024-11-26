import pygame

pygame.mixer.init()

arquivo_mp3 = "C:\Users\igorv\Music\tribodaperiferia-imprevisivel-2ad746d1.mp3"
pygame.mixer.music.load(arquivo_mp3)

# Reproduz o arquivo
pygame.mixer.music.play()

# Mantém o programa em execução enquanto o áudio toca
print("Reproduzindo... Pressione Enter para sair.")
input()