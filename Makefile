VM_IMAGE=$(HOME)/chr-7.12.1.img
SSH_PORT=2222
SSH_USER=admin
SSH_HOST=127.0.0.1

.PHONY: help vm connect app test-interface clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make vm         - Inicia a máquina virtual do MikroTik (QEMU)"
	@echo "  make connect    - Abre a sessão SSH com o MikroTik"
	@echo "  make app        - Inicia a aplicação Flask"
	@echo "  make check      - Checa as interfaces configuradas no MikroTik"

vm:
	sudo qemu-system-x86_64 -m 128M -smp 1 -drive file=$(VM_IMAGE),format=raw -net nic,model=virtio -net user,hostfwd=tcp::$(SSH_PORT)-:22 -nographic

connect:
	ssh -p $(SSH_PORT) $(SSH_USER)@$(SSH_HOST)

app:
	python app.py

check:
	ssh -p $(SSH_PORT) $(SSH_USER)@$(SSH_HOST) "/interface print detail"