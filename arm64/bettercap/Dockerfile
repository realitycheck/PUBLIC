# bettercap@v2.41.0
# DOCKER_BUILDKIT=1 docker build -f Dockerfile -o . .
FROM golang:1.24-bookworm as build

ENV GNU_HOST=aarch64-linux-gnu
ENV CC=$GNU_HOST-gcc
ENV PKG_CONFIG_PATH=/usr/lib/$GNU_HOST/pkgconfig

ENV GOARCH=arm64
ENV GOOS=linux
ENV CGO_ENABLED=1

RUN dpkg --add-architecture $GOARCH

RUN apt-get update && \
  apt-get --no-install-recommends install -y gcc-$GNU_HOST \
    libc6-dev-arm64-cross \
    libpcap-dev:$GOARCH libnetfilter-queue-dev:$GOARCH libusb-1.0-0-dev:$GOARCH && \
  rm -rf /var/lib/apt/lists/*

WORKDIR $GOPATH/src/github.com/bettercap/bettercap
ADD . .

RUN go build -o bettercap .

FROM scratch

COPY --from=build /go/src/github.com/bettercap/bettercap/bettercap /
