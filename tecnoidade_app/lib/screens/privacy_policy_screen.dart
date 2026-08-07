import 'package:flutter/material.dart';
import '../widgets/wavy_background.dart';

class PrivacyPolicyScreen extends StatelessWidget {
  const PrivacyPolicyScreen({super.key});

  @override
  Widget build(BuildContext context) {
    const textColor = Color(0xFF333333);
    const primaryBlue = Color(0xFF3A45B8);
    const bgSection = Color(0xFFC6DDF6);
    const darkGray = Color(0xFF444444);

    return WavyBackground(
      child: SingleChildScrollView(
        padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header
            Row(
              children: [
                InkWell(
                  onTap: () => Navigator.of(context).pop(),
                  borderRadius: BorderRadius.circular(20),
                  child: Container(
                    width: 40,
                    height: 40,
                    decoration: const BoxDecoration(
                      color: Colors.white,
                      shape: BoxShape.circle,
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black12,
                          blurRadius: 5,
                          offset: Offset(0, 2),
                        )
                      ],
                    ),
                    child: const Icon(
                      Icons.arrow_back_ios_new,
                      color: primaryBlue,
                      size: 20,
                    ),
                  ),
                ),
                const SizedBox(width: 15),
                const Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Política de Privacidade',
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: FontWeight.w800,
                          color: textColor,
                        ),
                        softWrap: true,
                      ),
                      Text(
                        'LGPD - Lei n° 13.709/2018',
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w800,
                          color: Color(0xFF555555),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 25),

            // Highlight Section
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: bgSection,
                borderRadius: BorderRadius.circular(8),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Conformidade com a LGPD',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w800,
                      color: darkGray,
                    ),
                  ),
                  SizedBox(height: 10),
                  Text(
                    'Esta política está alinhada a Lei Geral de Proteção de Dados Pessoais (LGPD - Lei n° 13.709/2018) e ao Marco Civil da internet (Lei n° 12.965/2014).',
                    style: TextStyle(
                      fontSize: 14,
                      fontWeight: FontWeight.w700,
                      color: darkGray,
                      height: 1.5,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 25),

            // Policy Content
            const Text(
              'Política de Privacidade – Aplicativo TecnoIdade',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              'Última atualização: Julho de 2026',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 25),

            const Text(
              '1. Apresentação',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 15),
            const Text(
              'A presente Política de Privacidade tem como objetivo explicar como o TecnoIdade coleta, utiliza, armazena e protege as informações dos usuários.',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: darkGray,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              'A privacidade e a segurança dos dados são prioridades do TecnoIdade, que atua em conformidade com os princípios estabelecidos pela Lei Geral de Proteção de Dados Pessoais (LGPD – Lei n° 13.709/2018).',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: darkGray,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              'Ao utilizar o aplicativo, o usuário declara estar ciente das práticas descritas nesta Política.',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: darkGray,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 25),

            const Text(
              '2. Dados Coletados',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 15),
            const Text(
              'Para oferecer uma melhor experiência, o TecnoIdade poderá coletar algumas informações, tais como:',
              style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
                color: darkGray,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 15),
            const Text(
              'Dados fornecidos pelo usuário',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w800,
                color: darkGray,
              ),
            ),
            const SizedBox(height: 15),
            
            // List Items
            _buildListItem('Nome completo;'),
            _buildListItem('Endereço de e-mail;'),
            _buildListItem('Senha de acesso (armazenada de forma segura);'),
            
            const SizedBox(height: 40),
          ],
        ),
      ),
    );
  }

  Widget _buildListItem(String text) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 15.0, left: 10.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Padding(
            padding: EdgeInsets.only(top: 6.0),
            child: Icon(
              Icons.circle,
              size: 6,
              color: Color(0xFF444444),
            ),
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Text(
              text,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w800,
                color: Color(0xFF444444),
                height: 1.5,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
