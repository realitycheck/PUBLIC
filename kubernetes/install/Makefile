kind-download:
	curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64


kind-install:
	install -o root -g root -m 0755 kind /usr/local/bin/kind


kubectl-download:
	curl -LO https://dl.k8s.io/release/v1.29.2/bin/linux/amd64/kubectl
	curl -LO https://dl.k8s.io/release/v1.29.2/bin/linux/amd64/kubectl.sha256
	echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check

kubectl-install:
	install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl


minikube-download:
	curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64


minikube-install:
	install -o root -g root -m 0755 minikube-linux-amd64 /usr/local/bin/minikube


minikube-start:
	minikube start --kubernetes-version=v1.28.3 --driver=dockerli


helm-download:
	wget https://get.helm.sh/helm-v3.14.3-linux-amd64.tar.gz
	tar -zxvf helm-v3.14.3-linux-amd64.tar.gz --strip-components=1


helm-install:
	install -o root -g root -m 0755 helm /usr/local/bin/helm
