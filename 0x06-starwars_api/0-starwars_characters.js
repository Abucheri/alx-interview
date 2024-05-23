#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  if (!characters || characters.length === 0) {
    console.error('No characters found for this movie.');
    process.exit(1);
  }

  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character data:', error);
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Failed to fetch character data. Status code:', response.statusCode);
          reject(new Error(`Status code: ${response.statusCode}`));
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
        resolve();
      });
    });
  }
});
