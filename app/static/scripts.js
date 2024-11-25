function toggleDetail(classId) {
    var detail = document.getElementById(classId);
    if (detail.style.display === "block") {
      detail.style.display = "none";
    } else {
      detail.style.display = "block";
    }
  }
  
  let count = 1;
  let playerTurn; // プレイヤーのターンを管理する変数
  
  function startCounting() {
    // 隠しボタンを非表示にする
    document.getElementById("hiddenButton").style.display = "none";
  
    // カウント30ゲームのポップアップを表示する
    document.getElementById("count30Popup").style.display = "block";
  
    // 先攻後攻をランダムに決定
    playerTurn = Math.random() < 0.5 ? 'player' : 'computer';
    document.getElementById("turn").textContent = playerTurn === 'player' ? 'あなたの番です' : 'コンピューターの番です';
  
    // 先攻がコンピューターの場合は、コンピューターにカウントさせる
    if (playerTurn === 'computer') {
      setTimeout(computerTurn, 1000);
    }
  }
  
  function countUp(num) {
    count += num;
    document.getElementById("count").textContent = count;
  
    // 30を言ったら負け
    if (count >= 30) {
      alert(playerTurn === 'player' ? 'あなたの負けです！' : 'あなたの勝ちです！');
      resetGame();
      return;
    }
  
    // プレイヤーとコンピューターのターンを切り替える
    playerTurn = playerTurn === 'player' ? 'computer' : 'player';
    document.getElementById("turn").textContent = playerTurn === 'player' ? 'あなたの番です' : 'コンピューターの番です';
  
    // コンピューターのターン
    if (playerTurn === 'computer') {
      setTimeout(computerTurn, 1000); // 1秒後にコンピューターにカウントさせる
    }
  }
  
  function computerTurn() {
    // コンピューターはランダムに1〜3をカウントアップする
    const num = Math.floor(Math.random() * 3) + 1;
    countUp(num);
  }
  
  function resetGame() {
    count = 1;
    document.getElementById("count30Popup").style.display = "none";
    document.getElementById("hiddenButton").style.display = "block"; // 隠しボタンを再表示
  }
  
  function showHiddenButton() {
    document.getElementById("hiddenButton").style.display = "block";
    document.getElementById("hiddenButton").onclick = startCounting; // 隠しボタンを押したらカウント30ゲームを開始
  }
  
  // ページ読み込み時に実行
  window.onload = function() {
    setTimeout(showHiddenButton, 10000); // 10秒後に隠しボタンを表示
  };