import controller
import logging
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scr/app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("Запуск приложения...")
    try:
        # Убедитесь, что use_https=False если не настроены SSL сертификаты
        server = controller.controller(port="8000", use_https=1, token_use=True)
        server.run()
    except Exception as e:
        logger.critical(f"Критическая ошибка при запуске сервера: {e}", exc_info=True)
        print(f"Критическая ошибка: {e}")
        time.sleep(5)  # Даем время прочитать сообщение об ошибке