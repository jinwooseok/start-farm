import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000'; // 혹은 본인의 서버 URL

const fetcher = async (method, url, ...rest) => {
    const res = await axios[method](url, ...rest);

    return res.data
};

export default fetcher;