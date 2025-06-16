build_website() {
    hugo -d public_html
}
upload() {
    # This command can also be used to simply recursively copy all files
    # id does not filter duplicates and thus takes a long time
    scp -r public_html pleyern@www461.your-server.de:/

    #     sftp pleyern@www461.your-server.de <<EOF
    #     put -R $cwd/public_html
    #     exit
    # EOF
    cd ..
}

build_website
upload
