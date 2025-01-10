document.addEventListener("DOMContentLoaded", () => {
    const mainRequest = document.getElementById("mainRequest");
    const subRequestContainer = document.getElementById("subRequestContainer");
    const subRequest = document.getElementById("subRequest");
    const submitButton = document.getElementById("submitButton");
    const result = document.getElementById("result");

    // メインが選択されたらサブ選択肢をリクエスト
    mainRequest.addEventListener("change", () => {
        const selectedRequest = mainRequest.value;
        if (selectedRequest) {
            // サーバーにサブ選択肢をリクエスト
            fetch("/get_sub_requests", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ mainRequest: selectedRequest })
            })
            .then(response => response.json())
            .then(options => {
                // サブ選択肢を表示
                subRequestContainer.style.display = "block";
                submitButton.style.display = "block";

                // サブ選択肢をリセットして更新
                subRequest.innerHTML = `<option value="" disabled selected>選択してください</option>`;
                Object.keys(options).forEach(option => {
                    const opt = document.createElement("option");
                    opt.value = option;
                    opt.textContent = option;
                    subRequest.appendChild(opt);
                });
            });
        }
    });

    // 提案ボタンが押されたらカメラを提案
    submitButton.addEventListener("click", () => {
        const mainRequestValue = mainRequest.value;
        const subRequestValue = subRequest.value;

        if (mainRequestValue && subRequestValue) {
            // サーバーの選択肢とサブ選択肢を送信
            fetch("/get_camera_recommendation", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    mainRequest: mainRequestValue,
                    subRequest: subRequestValue
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data); 
                // カメラを表示
                result.innerHTML = `
                    あなたにぴったりのレンズは「${data.camera}」です。<br>
                    ${data.feature}<br>
                    <img src="${data.photo}" alt="${data.camera}" style="max-width: 100%; height: auto;">
                `;
            });
        } else {
            result.textContent = "すべての選択肢を選んでください。";
        }
    });
});
