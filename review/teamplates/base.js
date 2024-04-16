const apiUrl = '/api/songs/';
const songList = document.querySelector('#song-list');

// 로딩 표시
songList.innerHTML = '<p>Loading...</p>';

// API 요청 
fetch(apiUrl)
    .then(response => {
        // 응답이 성공적으로 완료될 경우
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        // 응답을 JSON 형태로 파싱하여 반환
        return response.json();
    })
    .then(data => {
        // 받아온 데이터를 처리하여 화면에 표시
        renderSongs(data);
    })
    .catch(error => {
        // 오류 발생 시 에러 메시지를 화면에 표시
        songList.innerHTML = `<p>Error: ${error.message}</p>`;
    });

// 데이터를 화면에 표시하는 함수
function renderSongs(songs) {
    // 로딩 표시 제거
    songList.innerHTML = '';
    // 음악 데이터를 받아와서 HTML로 화면에 추가
    songs.forEach(song => {
        const listItem = document.createElement('li');
        listItem.textContent = `${song.title} by ${song.artist}`;
        songList.appendChild(listItem);
    });
}
