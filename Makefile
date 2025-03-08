.PHONY: all setup generate-data run-pipeline clean lint format test

# 默认任务： 设置环境、生成数据并运行管道
all: setup generate-data run-pipeline

# 设置环境
setup:
	docker compose build
	docker compose up -d
	@echo "环境设置完成，容器已启动"

# 生成数据
generate-data:
	docker compose exec data_engine poetry run python -m src.data.generate_sample_data
	@echo "数据生成完成"

# 运行管道
run-pipeline:
	docker compose exec data_engine bash scripts/run_pipeline.sh
	@echo "管道运行完成"

# 清理
clean:
	rm -rf data/processed/* data/final/* logs/*.logs
	@echo "已清理数据和日志"

# 格式化代码
format:
	docker compose exec data_engine poetry run black src
	docker compose exec data_engine poetry run isort src
	@echo "代码格式化完成"

# 代码检查
lint:
	docker compose exec data_engine poetry run flake8 src
	@echo "代码检查完成"

# 测试
test:
	docker compose exec data_engine poetry run pytest
	@echo "测试完成"

# 运行单元测试
test-unit:
	docker compose exec data_engine poetry run pytest src/tests/
	@echo "单元测试完成"

# 运行测试并生成覆盖率报告
test-coverage:
	docker compose exec data_engine poetry run pytest --cov=src src/tests/ --cov-report=term --cov-report=html
	@echo "测试覆盖率报告已生成"

