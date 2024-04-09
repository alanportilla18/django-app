import React, { useState, useEffect } from 'react';
import axios from 'axios';
const Planets = () => {
    const [planets, setPlanets] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get('https://api.nasa.gov/planetary/apod?api_key=5pmYxZELNaKrrxMqAcoCKxVQZf4HgXghzShyO4w2');
            setPlanets([response.data]);
        };
        fetchData();
    }, []);
    return (
        <div>
            <h1 className="text-3xl font-bold mb-4">Planets Data</h1>
            <div>
                {planets.map((planet, index) => (
                    <>
                    <div key={index} className="bg-gray-200 p-4 mb-4">
                        <h2 className="text-xl font-bold">{planet.title}</h2>
                        <img src={planet.url} alt={planet.title} className="w-full mt-2" />
                        <p className="mt-2">{planet.explanation}</p>
                    </div>
Cesmag University - Engineering faculty
Teacher Joan</>
                ))}
            </div>
        </div>
    );
};
export default Planets;
