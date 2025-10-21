FROM debian:bullseye

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    git python3 python3-pip i2c-tools && \
    pip3 install psutil && \
    apt-get clean

# Clone the ABS Mini Tower Kit repo
RUN git clone https://github.com/geeekpi/absminitowerkit.git /opt/absminitower

# Set working directory
WORKDIR /opt/absminitower

# Make run script executable
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
