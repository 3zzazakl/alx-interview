#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi.co/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

const movieData = JSON.parse(body);

const characterUrls = movieData.characters;

    characterUrls.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.log(error);
                return;
            }
            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});
