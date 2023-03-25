# HackNight-UPC

# Col·laborar:
## 1. Generar clau SSH
```ssh-keygen -t ed25519 -C "[CORREU DE GITHUB]"```
## 2. Copiar-la
```cat ~/.ssh/id_ed25519.pub```
o el directori on s'hagi generat la clau
## 3. Afegir la clau al GitHub
Settings -> SSH and GPG keys -> New SSH key -> enganxar la clau
## 4. Afegir la clau SSH localment 
o algo així 
```eval `ssh-agent -s` ```
```ssh-add```
## 5. Clonar el repositori
```git clone https://github.com/Elahi-cs/HackNight-UPC/```
## 6. Settejar la url del SSH
```git remote set-url origin git@github.com:Elahi-cs/HackNight-UPC.git```

Projecte de referència: [Sideways Shooter](https://github.com/Elahi-cs/Sideways-Shooter)
