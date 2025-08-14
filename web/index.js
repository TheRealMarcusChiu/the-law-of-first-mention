const books = [
  "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth",
  "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra",
  "Nehemiah", "Esther", "Job", "Psalm", "Proverbs", "Ecclesiastes", "Song Of Solomon",
  "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
  "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah",
  "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
  "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians",
  "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
  "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"
];

let firstOccurrences = {};

async function loadData() {
    const res = await fetch('bibles/esv-out.txt');
    const text = await res.text();
    const lines = text.split(/\r?\n/);
    lines.forEach(line => {
        if (!line.trim()) return;
        const [word, bookNum, chapterVerse] = line.trim().split(/\s+/);
        const bookName = books[parseInt(bookNum)];
        firstOccurrences[word.toLowerCase()] = `${bookName} ${chapterVerse}`;
    });
}

function findWord(){
  const inputEl = document.getElementById('wordInput');
  const resultBox = document.getElementById('resultBox');
  const raw = inputEl.value.trim();
  if(!raw){ resultBox.textContent = 'Please enter a word.'; return; }
  const key = raw.toLowerCase();
  const where = firstOccurrences[key];
  resultBox.textContent = where ? `"${key}" first appears in ${where}` : `"${key}" was not found :(`;
}

document.getElementById('findBtn').addEventListener('click', findWord);
document.getElementById('wordInput').addEventListener('keydown', e => { if(e.key === 'Enter') findWord(); });

loadData();
