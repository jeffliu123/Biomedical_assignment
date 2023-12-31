if [ -d "./ECG_data" ]; then
    echo "You have downloaded the dataset"
else
    echo "Downloading the models..."
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1Sohvsv3Fe3RMcVfbGv_UE5rnt54CmgTk' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1Sohvsv3Fe3RMcVfbGv_UE5rnt54CmgTk" -O ./ECG_data.zip && rm -rf /tmp/cookies.txt
    unzip ECG_data.zip && rm -rf ECG_data.zip
    echo "Finished ! "
fi
