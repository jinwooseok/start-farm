import axios from 'axios';
const serverUrl = process.env.REACT_APP_SERVER_URL;
axios.defaults.baseURL = serverUrl; // 혹은 본인의 서버

const fetcher = async (method, url, ...rest) => {
    const res = await axios[method](url, ...rest);

    return res.data
};

export default fetcher;