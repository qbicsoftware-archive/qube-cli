package life.qbic.portal.portlet

import spock.lang.Specification

class {{ cookiecutter.main_class_prefix }}Test extends Specification{

    def "first test"(){
        when:
        def value = 2+2
        then:
        value == 4
    }

}
