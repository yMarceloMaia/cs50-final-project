const counter = document.getElementById('counter');
let recordingCounter = 0;
let intervalId;
let activated = false

function clearCounter() {
    clearInterval(intervalId)
}

function updateCounter() {
    recordingCounter = recordingCounter + 1;
    counter.innerHTML = `Translating... ${recordingCounter} seconds`;
};


function startRecording() {
    activated = true
    clearCounter()
    const p = document.getElementById('hold-p')
    if (p.innerHTML === '') p.innerHTML = "Hold space to record"

    const button = document.getElementById('start-recording');
    button.disabled = true;

    window.addEventListener('keydown', (e) => handleKeyPress(e, true));
    window.addEventListener('keyup', (e) => handleKeyPress(e, false));


    fetch('/start_recording')
        .then(response => response.text())
        .then(data => {
            counter.innerHTML = "Its done"
            recordingCounter = 0

            const audioElement = new Audio("");
            audioElement.controls = true;

            setTimeout(() => {
                getAudio()
            }, "1000");
        }).catch((error) => {
            console.log(error)
            counter.innerHTML = "Error"
            recordingCounter = 0
        }).finally(() => {
            button.disabled = false
            clearCounter()
            activated = false
            return
        })
}

function getAudio() {
    fetch('/get_audio')
        .then(response => response.blob())
        .then(blob => {
            const audioUrl = URL.createObjectURL(blob);
            const audioPlayer = document.getElementById('audioPlayer');
            audioPlayer.src = audioUrl;
        }).catch((error) => {
            console.log(error)
        });
}

const handleKeyPress = (e, recording) => {
    const keyCode = e.which || e.keyCode || 0;
    const space = keyCode === 32;
    const p = document.getElementById('hold-p');

    if (space) {
        p.innerHTML = recording && activated ? 'Recording' : 'Recording stopped';
        if (!recording) {
            clearCounter()
            intervalId = setInterval(updateCounter, 1000)
        }
    }
};

