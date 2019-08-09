       window.addEventListener('load', function () {
            const codeReader = new ZXing.BrowserQRCodeReader()
            console.log('ZXing code reader initialized')
            codeReader.getVideoInputDevices()
                .then((videoInputDevices) => {

                    const firstDeviceId = videoInputDevices[0].deviceId

                    document.getElementById('screenshot-button').addEventListener('click', () => {
                        codeReader.decodeFromInputVideoDevice(firstDeviceId, 'video').then((result) => {
                            console.log(result)
                            document.getElementById('result').textContent = result.text
                        }).catch((err) => {
                            console.error(err)
                            document.getElementById('result').textContent = err
                        })
                        console.log(`Started continous decode from camera with id ${firstDeviceId}`)
                    })


                })
                .catch((err) => {
                    console.error(err)
                })
        })



        window.addEventListener('load', function () {
            const codeReader = new ZXing.BrowserQRCodeReader('video')
            console.log('ZXing code reader initialized')
                

            document.getElementById('screenshot-button').addEventListener('click', () => {
                const img = document.querySelector('#screenshot-img');
                const video = document.querySelector('#screenshot-video');

                const canvas = document.createElement('canvas');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0);
                img.src = canvas.toDataURL('image/jpeg');
                console.log('video src');
                console.log(video.videoHeight);
                codeReader.decodeFromImage(img).then((result) => {
                    
                    console.log(result)
                    document.getElementById('result').textContent = result.text
                }).catch((err) => {
                    console.error(err)
                    console.log("error");
                    document.getElementById('result').textContent = 'err'
                })
                console.log(`Started decode for image from ${img.src}`)
            })

        })