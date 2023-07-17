
const searchForm = document.getElementById('titleForm');

searchForm.addEventListener('submit', (event) => {
    event.preventDefault();
    console.log(2)

    const searchInput = document.getElementById('searchInput');
    const searchTerm = searchInput.value.trim();

    if (searchTerm !== '') {
        window.location.href = '/search/title?title=' + encodeURIComponent(searchTerm);
    }
});
