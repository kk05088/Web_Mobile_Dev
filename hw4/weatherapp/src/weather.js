

import React, { useEffect, useState } from "react";
import { View, Text, TextInput, StyleSheet } from "react-native";

function Weather() {
  const [inputValue, setInputValue] = useState("");
  const [data, setData] = useState(null);
  const [city, setCity] = useState("");
  const API_KEY = "2fce26b3009e0a66de8c0a0223800869";

  // function get temp data
  const getTempData = (api, query) => {
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${query}&units=metric&appid=${api}`;
    fetch(url)
      .then((res) => {
        return res.json();
      })
      .then((res) => {
        setData(res.main);
        setCity(query);
        // console.log(res.main);
      })
      .catch((err) => {
        console.log("error in get data", err);
        setData(null);
      });
  };

  // call use Effect for render data every search input
  useEffect(() => {
    getTempData(API_KEY, inputValue);
  }, [inputValue]);

  return (
    <View>WELCOME TO OUR WEATHER APP
      <TextInput
        style={styles.input}
        placeholder="Enter City Name"
        value={inputValue}
        onChangeText={(text) => setInputValue(text)}
      />
      
      {!inputValue.length ? null : data ? (
        <View>
          <Text style={styles.city}>Weather Details of City : {city}</Text>
          
          <View style={styles.infoContainer}>
            <Text>Current Temperature : {data.temp} °C</Text>
            <Text>Feels Like : {data.feels_like}</Text>
            <Text>Temperature Min : {data.temp_min} °C</Text>
            <Text>Temperature Max : {data.temp_max} °C</Text>
            <Text>Humidity  : {data.humidity}</Text>
            <Text>pressure  : {data.pressure} pa</Text>
          </View>
        </View>
      ) : (
        <Text style={styles.validCity}>Enter Valid City Name</Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  input: {
    borderWidth: 1,
    borderColor: "gray",
    margin: 10,
    padding: 5,
  },
  city: {
    fontSize: 20,
    fontWeight: "bold",
    marginVertical: 10,
  },
  infoContainer: {
    margin: 10,
  },
  validCity: {
    color: "red",
    margin: 10,
  },
});

export default Weather;