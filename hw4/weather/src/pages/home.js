import { View, Text, StyleSheet } from "react-native"

export default () => {
    return (<View style={styles.container}>
        <Text>Welcome to Todo app</Text>
    </View>)
}
const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center"
    }
})