setup:
	@python3 -m pip install --quiet --disable-pip-version-check --requirement requirements.txt
	@python3 -c 'import ledger_formatting'
