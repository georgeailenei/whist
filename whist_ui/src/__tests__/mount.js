import { render } from '@testing-library/vue'
import Controller from '../components/Controller.vue'

test ('Testing Controller Component', () => {
    const {getByText} = render(Controller);
})
